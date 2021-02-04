from Kiraro import bot
from discord.ext import commands
import discord
import aiohttp
import random
import json
import requests
import sysconfig
import logging
import logger
from pyfiglet import figlet_format, FontNotFound



@bot.command()
async def meme(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            embed = discord.Embed(title="", description="", colour=discord.Colour.blue())
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)


@bot.command()
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
async def joke(ctx):
    response = json.loads(requests.get("https://tambalapi.herokuapp.com").text)
    await ctx.send(content=response[random.randint(0, len(response) - 1)]["joke"])


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


@bot.command(aliases=['coinflip', 'coin_flip'])
async def coin(ctx):
    value = random.choice(['heads', 'tails'])
    await ctx.send(F"You got {value}")


@bot.command()
async def givenum(ctx, x: int = 0, y: int = 100):
    if x < y:
        value = random.randint(x, y)
        await ctx.send(f"You got **{value}**.")
    else:
        await ctx.send(":warning: Please ensure the first number is smaller than the second number.")


@givenum.error
async def givenum_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please only enter a number")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="GiveNum",
            description="To use the GiveNum command add a 2 number",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="GiveNum `num` `num`")
        await ctx.send(embed=embed)
    else:
        print(F"GiveNum Error {error}")


@bot.command(aliases=['ud'])
async def urban(ctx, *msg):
    try:
        word = ' '.join(msg)
        api = "http://api.urbandictionary.com/v0/define"
        logging.info("Making request to " + api)
        response = requests.get(api, params=[("term", word)]).json()
        embed = discord.Embed(description="No results found!", colour=0xFF0000)
        if len(response["list"]) == 0:
            return await ctx.send(embed=embed)
        embed = discord.Embed(title="Word", description=word, colour=embed.colour)
        embed.add_field(name="Top definition:", value=response['list'][0]['definition'])
        embed.add_field(name="Examples:", value=response['list'][0]['example'])
        await ctx.send(embed=embed)
    except:
        await ctx.send('well thats... thats... thats weird i cant connect to urban dictionary please try again later')

        
@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
    embed = discord.Embed(color=0x00aaff)
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=random.choice(responses), inline=True)
    await ctx.send(embed=embed)