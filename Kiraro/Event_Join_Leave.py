import discord
from Kiraro import bot
import json
import time


@bot.event
async def on_member_join(member: discord.member):
    try:
        with open("Files/Stats.json", "r") as f:
            stats = json.load(f)
        channel = bot.get_channel(stats[str(member.guild.id)])
        await channel.edit(name=F"All Members: {member.guild.member_count}")
    except KeyError:
        pass
    try:
        with open("Files/join_leave.json") as f:
            join = json.load(f)
        server = join[str(member.guild.id)]
        channel = bot.get_channel(server['welcome'])
        embed = discord.Embed(
            title=F"Welcome to {member.guild}, Get started by looking through the announcements channels and info channels!",
            color=0x0000ff)
        embed.set_author(name=F"{member.name} Welcome to {member.guild}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=F"{member.guild} | Member count: {member.guild.member_count} | {time.asctime()}")
        await channel.send(embed=embed)
    except KeyError:
        pass


@bot.event
async def on_member_remove(member: discord.member):
    try:
        with open("Files/Stats.json") as f:
            stats = json.load(f)
        channel = bot.get_channel(stats[str(member.guild.id)])
        await channel.edit(name=F"All Members: {member.guild.member_count}")
    except KeyError:
        pass
    try:
        with open("Files/join_leave.json") as f:
            leave = json.load(f)
        server = leave[str(member.guild.id)]
        channel = bot.get_channel(server['goodbye'])
        embed = discord.Embed(
            title=F"Goodbye {member}, You will be missed, or maybe not we don't know. ¯\_(ツ)_/¯",
            color=0xff0000)
        embed.set_author(name=F"{member} left {member.guild}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=F"{member.guild} | Member count: {member.guild.member_count} | {time.asctime()}")
        await channel.send(embed=embed)
    except KeyError:
        pass
