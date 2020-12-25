import discord
from discord.ext import commands
from Kiraro import bot, Cooldown
import json
import time


@bot.event
async def on_message(message):
    mentions = [str(m) for m in message.mentions]
    if str(bot.user) in list(mentions):
        channel = bot.get_channel(message.channel.id)
        with open("Files/Prefix.json") as f:
            prefixes = json.load(f)
        prefix = prefixes.get(str(message.guild.id))
        await channel.send(F"***My prefix is*** `{prefix}`")
    with open("Files/Stop_Start_Rank.json") as f:
        stop_start = json.load(f)
    server = stop_start[str(message.guild.id)]
    if server["text"]:
        if not message.author.bot:
            if await Cooldown(message, 5):
                with open("Files/TextRanking.json", "r") as f:
                    rank = json.load(f)
                try:
                    test = rank[str(message.guild.id)]
                    new_user = True
                    for x in test['users']:
                        if x["name"] == str(message.author.mention):
                            x['message'] += 1
                            x['xp'] += 3
                            if x['xp'] >= x['next_xp']:
                                x['xp'] = (x['xp'] - x['next_xp'])
                                x['next_xp'] += 100
                                x['level'] += 1
                                channel = bot.get_channel(message.channel.id)
                                await channel.send(F"{message.author.mention} congrats you are now level {x['level']}")
                            new_user = False
                            break
                    if new_user:
                        test['users'].append({
                            'name': str(message.author.mention),
                            'xp': 3,
                            'next_xp': 100,
                            'level': 0,
                            'message': 1
                        })
                except KeyError:
                    rank[str(message.guild.id)] = {"users": []}
                    test = rank[str(message.guild.id)]
                    test['users'].append({
                        'name': str(message.author.mention),
                        'xp': 3,
                        'next_xp': 100,
                        'level': 0,
                        'message': 1
                    })
                with open("Files/TextRanking.json", "w") as f:
                    json.dump(rank, f, indent=4)
    await bot.process_commands(message)



@bot.event
async def on_voice_state_update(member, before, after):
    with open("Files/Stop_Start_Rank.json") as f:
        stop_start = json.load(f)
    server = stop_start[str(member.guild.id)]
    if server["voice"]:
        if not member.bot:
            with open("Files/VoiceRanking.json", "r") as f:
                rank = json.load(f)
            in_channel = before.channel and after.channel
            if not before.channel:
                try:
                    server = rank[str(member.guild.id)]
                    new_user = True
                    for x in server['users']:
                        if x["name"] == str(member.mention):
                            x['time'] = time.time()
                            new_user = False
                            break
                    if new_user:
                        server['users'].append({
                            'name': str(member.mention),
                            'time_sec': 0,
                            'time': time.time(),
                            'hours': 0,
                            'seconds': 0
                        })
                except KeyError:
                    rank[str(member.guild.id)] = {"users": []}
                    server = rank[str(member.guild.id)]
                    server['users'].append({
                        'name': str(member.mention),
                        'time_sec': 0,
                        'time': time.time(),
                        'hours': 0,
                        'seconds': 0
                    })
            server = rank[str(member.guild.id)]
            for x in server['users']:
                if x["name"] == str(member.mention):
                    if before.channel and not after.channel:
                        if x['time'] != 0:
                            x['time_sec'] = abs(x['time'] - time.time()) + x['time_sec']
                            x['seconds'] += x['time_sec']
                            while x['time_sec'] >= (3600 * (x['hours'] + 1)):
                                x['hours'] += 1
                                x['time_sec'] -= 3600
                            x['time'] = 0
                    elif in_channel and member.voice.deaf or member.voice.self_deaf or member.voice.mute or member.voice.self_mute or member.voice.afk:
                        if x['time'] != 0:
                            x["time_sec"] = abs(x['time'] - time.time()) + x['time_sec']
                            x['time'] = 0
                    elif in_channel and before.deaf or before.self_deaf or before.mute or before.self_mute or before.afk:
                        x['time'] = time.time()
            with open("Files/VoiceRanking.json", "w") as f:
                json.dump(rank, f, indent=4)