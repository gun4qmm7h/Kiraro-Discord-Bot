from Kiraro import bot
from discord.ext import commands
import discord
import aiohttp
import random
import json
import requests

@bot.command(pass_context=True)
async def meme(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            embed = discord.Embed(title="", description="", colour=discord.Colour.blue())
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)


@bot.command(pass_content=True)
async def nsfw(ctx):
    if ctx.channel.is_nsfw():
        embed = discord.Embed(title="", description="", colour=discord.Colour.blue())
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/nsfw/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'][random.randint(0, 24)]['data']['url'])
                await ctx.send(embed=embed)
    else:
        await ctx.send("This Channel is not mark as nsfw")




@bot.command()
@commands.has_permissions(manage_channels=True)
async def hide(ctx):
    ow = ctx.channel.overwrites_for(ctx.guild.default_role)
    if ow.send_messages or ow.send_messages is None:
        perms = ctx.channel.overwrites_for(ctx.guild.default_role)
        perms.send_messages = False
        perms.view_channel = False
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=perms)
        await ctx.send("The channel has been hidden, nobody can see this chat, use the command again to un-hide")
    else:
        perms = ctx.channel.overwrites_for(ctx.guild.default_role)
        perms.send_messages = True
        perms.view_channel = True
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=perms)
        await ctx.send("The channel has been un-hidden :)")


@hide.error
async def hide_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Role Error",
            description="You are missing the **permission** `Manage Channels`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print(F"lockdown Error {error}")


@bot.command(pass_context=True)
async def joke(ctx):
    response = json.loads(requests.get("https://tambalapi.herokuapp.com").text)
    await ctx.send(content=response[random.randint(0, len(response)-1)]["joke"])


@bot.command()
async def size(ctx):
    value = random.randint(0, 18)
    if value == 0:
        await ctx.send(f'lol imagine not having pp you got {value} inches')
    elif value == 1:
        await ctx.send(f"lol imagine having {value} inch. couldn't be me-... oh wait im a bot. I don't have a pp")
    elif value == 12:
        await ctx.send(f"Dang my guy has a one footer coming in at {value} inches")
    elif value == 18:
        await ctx.send(f"ok this guy got {value} inches im just jealous at this point")
    else:
        await ctx.send(f"You have {value} inches.")