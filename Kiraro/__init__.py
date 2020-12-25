import discord
from discord.ext import commands
import hashlib
import asyncio
import json
import os
import sys
import time

cooldown = {}


def hash_lib(string):
    hash_name = hashlib.md5(string.encode())
    return hash_name.hexdigest()


def get_hours(sec):
    day = sec // (24 * 3600)
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    minutes = sec // 60
    sec %= 60
    second = sec
    if day != 0.0:
        if hour != 0:
            return F"{day}.{hour}d"
        return F"{day}d"
    elif hour != 0:
        if minutes != 0:
            return F"{hour}.{minutes}H"
        return F"{hour}H"
    elif minutes != 0.0:
        if second != 0:
            return F"{minutes}.{second}M"
        return F"{minutes}M"
    else:
        return F"{second}S"


def get_days(sec):
    day = sec // (24 * 3600)
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    minutes = sec // 60
    sec %= 60
    seconds = sec
    return F"{day}d, {hour}h, {minutes}m, {seconds}s"


def get_sec(time_str):
    try:
        sec1 = 0
        sec2 = 0
        sec3 = 0
        sec4 = 0
        for x in time_str.split(":"):
            if x[-1].lower() == "d":
                sec1 = 86400 * int(x[:-1])
            elif x[-1].lower() == "h":
                sec2 = 3600 * int(x[:-1])
            elif x[-1].lower() == "m":
                sec3 = 60 * int(x[:-1])
            elif x[-1].lower() == "s":
                sec4 = int(x[:-1])
        return sec1 + sec2 + sec3 + sec4
    except ValueError:
        return False


def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    try:
        return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])
    except IndexError:
        print("SOMEONE HAS GOT PASS RANK 99999999999999")



async def Cooldown(message, time_sleep):
    global cooldown
    if not bool(cooldown.get(message.author.mention)):
        cooldown[message.author.mention] = time.time() + time_sleep
        return False
    elif cooldown[message.author.mention] <= time.time():
        cooldown.pop(message.author.mention)
        return True

# Loads the discord server id to the .json file
def get_prefix(bot, message):
    with open("Files/Prefix.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


def is_us(user):
    user = hash_lib(user)
    us = ["6c947ced1e18cf3175f4219cf254f538", "baf94b182d2a1e1ba478d6c226f26112", "a65f4e316c842bd192089e065a98e691"]
    for x in range(len(us)):
        if user == us[x]:
            return True


async def TextRank(server, server_id):
    lst_msg = server['txt_message']
    channel = await bot.fetch_channel(lst_msg[0])
    msg = await channel.fetch_message(lst_msg[1])
    with open("Files/TextRanking.json", "r") as f:
        rank = json.load(f)
    server_rank = rank[str(server_id)]
    users = server_rank['users']
    name_dir = {}
    msg_num = []
    for x in users:
        name_dir[x["message"]] = [x['name'], x['xp'], x['level'], x['next_xp']]
        msg_num.append(x['message'])

    msg_num = sorted(msg_num, reverse=True)

    num = 1
    embed = discord.Embed(title="Text Rank Live Leaderboard", color=0x006eff)
    for i in msg_num:
        user_id = ''.join([i for i in name_dir[i][0] if i.isdigit()])
        user_name = bot.get_user(int(user_id))

        if user_name is None:
            break

        embed.add_field(name=F"#{num}: {user_name}",
                        value=F"***Xp***: {name_dir[i][1]}\n"
                              F"***Next Xp***: {name_dir[i][3]}\n"
                              F"***Level***: {name_dir[i][2]}\n"
                              F"***Message***: {i}",
                        inline=False)
        if num == lst_msg[2]:
            break
        num += 1
    embed.set_footer(text="This leaderboard will be updated every 30 seconds")
    await msg.edit(embed=embed)


async def VoiceRank(server, server_id):
    lst_msg = server['vc_message']
    channel = await bot.fetch_channel(lst_msg[0])
    msg = await channel.fetch_message(lst_msg[1])
    with open("Files/VoiceRanking.json") as f:
        voice = json.load(f)
    name_dir = {}

    sec = []
    server_voice = voice[str(server_id)]
    user = server_voice['users']
    for x in user:
        name_dir[x["time_sec"]] = [x['name']]
        sec.append(x['time_sec'])

    sec = sorted(sec, reverse=True)

    num = 1
    embed = discord.Embed(title="Voice Rank Leaderboard", color=0x006eff)
    for i in sec:
        user_id = ''.join([i for i in name_dir[i][0] if i.isdigit()])
        user_name = bot.get_user(int(user_id))
        if user_name is None:
            break

        embed.add_field(name=F"#{num}: {user_name}", value=F"***Time***: {get_days(round(i))}", inline=False)

        if num == lst_msg[2]:
            break
        num += 1
    embed.set_footer(text="This leaderboard will be updated every 30 seconds")
    await msg.edit(embed=embed)


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=intents)
bot.remove_command("help")


@bot.command()
async def Invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=577231380392706049&permissions=8&scope=bot")
    await asyncio.sleep(0.5)
