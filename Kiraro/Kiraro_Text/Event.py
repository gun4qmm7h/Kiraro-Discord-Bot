import discord
from Kiraro.Kiraro_Text import TextRank, VoiceRank, version
from Kiraro import bot
import json
import time
import asyncio


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("@ Me For Prefix"))

    with open("Files/Prefix.json", "r") as f:
        prefixes = json.load(f)

    with open("Files/Stop_Start_Rank.json") as f:
        stop_start = json.load(f)

    with open("Files/Live_Leaderboard.json") as f:
        livelb = json.load(f)

    with open("Files/TextRanking.json") as f:
        text = json.load(f)

    with open("Files/VoiceRanking.json") as f:
        voice = json.load(f)

    for guild in bot.guilds:
        if str(guild.id) not in prefixes:
            prefixes[str(guild.id)] = ">"

        if str(guild.id) not in stop_start:
            stop_start[str(guild.id)] = {}
            server = stop_start[str(guild.id)]
            server.update({"text": True,
                           "voice": True})

        if str(guild.id) not in livelb:
            livelb[str(guild.id)] = {}
            lb_server = livelb[str(guild.id)]
            lb_server.update({"text": False,
                              "voice": False,
                              "txt_message": [],
                              "vc_message": []})

        if str(guild.id) not in text:
            text[str(guild.id)] = {}
            text_rank = text[str(guild.id)]
            text_rank.update({"users": []})

        if str(guild.id) not in voice:
            voice[str(guild.id)] = {}
            voice_rank = voice[str(guild.id)]
            voice_rank.update({"users": []})

    with open("Files/Prefix.json", "w") as f:
        json.dump(prefixes, f, indent=4)

    with open("Files/Stop_Start_Rank.json", "w") as f:
        json.dump(stop_start, f, indent=4)

    with open("Files/Live_Leaderboard.json", "w") as f:
        json.dump(livelb, f, indent=4)

    with open("Files/TextRanking.json", "w") as f:
        json.dump(text, f, indent=4)

    with open("Files/VoiceRanking.json", "w") as f:
        json.dump(voice, f, indent=4)

    print(F"Bot is ready as {bot.user}. Servers: {len(bot.guilds)}. Date: {time.asctime()}. Version: {version}")

    while True:
        with open("Files/Live_Leaderboard.json") as f:
            livelb = json.load(f)
        for server_id in livelb:
            server = livelb[str(server_id)]
            if server["text"]:
                try:
                    lst_msg = server['txt_message']
                    channel = await bot.fetch_channel(lst_msg[0])
                    msg = await channel.fetch_message(lst_msg[1])
                    await TextRank(server_id, msg, lst_msg[2], live=True)
                except discord.errors.NotFound:
                    server.update({"text": False,
                                   "txt_message": []})
            if server["voice"]:
                try:
                    lst_msg = server['txt_message']
                    channel = await bot.fetch_channel(lst_msg[0])
                    msg = await channel.fetch_message(lst_msg[1])
                    await VoiceRank(server_id, msg, lst_msg[2], live=True)
                except discord.errors.NotFound:
                    server.update({"voice": False,
                                   "vc_message": []})
        with open("Files/Live_Leaderboard.json", "w") as f:
            json.dump(livelb, f, indent=4)
        await asyncio.sleep(30)


# Add a default prefix for every server
@bot.event
async def on_guild_join(guild):
    with open("Files/Prefix.json") as f:
        prefixes = json.load(f)

    with open("Files/Stop_Start_Rank.json") as f:
        stop_start = json.load(f)

    with open("Files/Live_Leaderboard.json") as f:
        livelb = json.load(f)

    with open("Files/TextRanking.json") as f:
        text = json.load(f)

    with open("Files/VoiceRanking.json") as f:
        voice = json.load(f)

    prefixes[str(guild.id)] = ">"

    stop_start[str(guild.id)] = {}
    server = stop_start[str(guild.id)]
    server.update({"text": True,
                   "voice": True})

    livelb[str(guild.id)] = {}
    lb_server = livelb[str(guild.id)]
    lb_server.update({"text": False,
                      "voice": False,
                      "txt_message": [],
                      "vc_message": []})

    text[str(guild.id)] = {}
    text_rank = text[str(guild.id)]
    text_rank.update({"users": []})


    voice[str(guild.id)] = {}
    voice_rank = voice[str(guild.id)]
    voice_rank.update({"users": []})

    with open("Files/Prefix.json", "w") as f:
        json.dump(prefixes, f, indent=4)

    with open("Files/Stop_Start_Rank.json", "w") as f:
        json.dump(stop_start, f, indent=4)

    with open("Files/Live_Leaderboard.json", "w") as f:
        json.dump(livelb, f, indent=4)

    with open("Files/TextRanking.json", "w") as f:
        json.dump(text, f, indent=4)

    with open("Files/VoiceRanking.json", "w") as f:
        json.dump(voice, f, indent=4)


# Removes the prefix for a server that removed the bot
@bot.event
async def on_guild_remove(guild):
    with open("Files/Prefix.json") as f:
        prefixes = json.load(f)

    with open("Files/Stop_Start_Rank.json") as f:
        stop_start = json.load(f)

    with open("Files/Live_Leaderboard.json") as f:
        livelb = json.load(f)

    with open("Files/TextRanking.json") as f:
        text = json.load(f)

    with open("Files/VoiceRanking.json") as f:
        voice = json.load(f)

    prefixes.pop(str(guild.id))

    stop_start.pop(str(guild.id))

    livelb.pop(str(guild.id))

    text.pop(str(guild.id))

    voice.pop(str(guild.id))

    with open("Files/Prefix.json", "w") as f:
        json.dump(prefixes, f, indent=4)

    with open("Files/Stop_Start_Rank.json", "w") as f:
        json.dump(stop_start, f, indent=4)

    with open("Files/Live_Leaderboard.json", "w") as f:
        json.dump(livelb, f, indent=4)

    with open("Files/TextRanking.json", "w") as f:
        json.dump(text, f, indent=4)

    with open("Files/VoiceRanking.json", "w") as f:
        json.dump(voice, f, indent=4)