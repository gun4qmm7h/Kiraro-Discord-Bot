import discord
from discord.ext import commands
from Kiraro import bot
import hashlib
import asyncio
import json
import time
import random

cooldown = {}
rand_xp = random.randint(15, 25)
xp_background = "Images/Xp_Background_With_Boarder.png"
us = ["a50efa1b366f80c5cd918dc243591465", "b52e451e257acd4e5b900bc183f6a1a3",
      "044320cd00a21e589a2579c6e3365d3e"]  # Mark, Jake, Jawad


def hash_lib(string):
    hash_name = hashlib.md5(str(string).encode())
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
        if cooldown.get(message.author.mention) is None:
            cooldown[message.author.mention] = time.time() + time_sleep
            return True
        else:
            return False
    elif cooldown[message.author.mention] <= time.time():
        cooldown.pop(message.author.mention)
        return True


async def is_us(user):
    user = hash_lib(user)
    for x in range(len(us)):
        if user == us[x]:
            return True

async def circle(draws, center, radius, fill):
    draws.ellipse((center[0] - radius + 1, center[1] - radius + 1,
                   center[0] + radius - 1, center[1] + radius - 1), fill=fill, outline=None)


async def TextRank(server_id, msg, number=10, live=False):
    low_user = False
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
    if live:
        embed = discord.Embed(title="Text Rank Live Leaderboard", color=0x006eff)
    else:
        embed = discord.Embed(title="Text Rank Leaderboard", color=0x006eff)
    embed.set_thumbnail(url=msg.guild.icon_url)
    for i in msg_num:
        user_id = ''.join([i for i in name_dir[i][0] if i.isdigit()])
        user_name = bot.get_user(int(user_id))

        if user_name is None:
            low_user = True
            break

        embed.add_field(name="ㅤ",  # This is a special space, normal ones won't work. Website: https://www.compart.com/en/unicode/U+3164
                        value=F"**__#{num}: {user_name.mention} __**\n"
                              F"Level: {name_dir[i][2]}\n"
                              F"Xp: {name_dir[i][1]}/{name_dir[i][3]}\n"
                              F"Message: {i}",
                        inline=False)
        if num == number:
            break
        num += 1
    if live:
        embed.set_footer(text="This leaderboard will be updated every 30 seconds")
    try:
        await msg.edit(embed=embed)
    except AttributeError:
        message = await msg.send(embed=embed)
        return message, low_user, name_dir


async def VoiceRank(server_id, msg, number=10, live=False):
    low_user = False
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
    if live:
        embed = discord.Embed(title="Voice Rank Live Leaderboard", color=0x006eff)
    else:
        embed = discord.Embed(title="Voice Rank Leaderboard", color=0x006eff)
    embed.set_thumbnail(url=msg.guild.icon_url)
    for i in sec:
        user_id = ''.join([i for i in name_dir[i][0] if i.isdigit()])
        user_name = bot.get_user(int(user_id))
        if user_name is None:
            low_user = True
            break

        embed.add_field(name="ㅤ",  # This is a special space, normal ones won't work. Website: https://www.compart.com/en/unicode/U+3164
                        value=F"**__#{num}: {user_name.mention}__**\n"
                              F"***Time***: {get_days(round(i))}",
                        inline=False)

        if num == number:
            break
        num += 1
    if live:
        embed.set_footer(text="This leaderboard will be updated every 30 seconds")
    try:
        await msg.edit(embed=embed)
    except AttributeError:
        message = await msg.send(embed=embed)
        return message, low_user, name_dir

@bot.command()
async def Invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=577231380392706049&permissions=8&scope=bot")
    await asyncio.sleep(0.5)


@bot.command()
async def invites(ctx):
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            totalInvites += i.uses
    await ctx.send(f"You've invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!")