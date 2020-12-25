import discord
from discord.ext import commands
from Kiraro import bot
import json


@bot.command(aliases=['suggest', 'sug'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def suggestions(ctx, *, suggestion):
    with open("Files/Suggestions.json", "r") as f:
        server = json.load(f)
    await ctx.send("the message has been sent")
    channel = bot.get_channel(server[str(ctx.guild.id)])
    embed = discord.Embed(title=F"{ctx.author} has a suggestions for the server", description=suggestion,
                          color=0x0080ff)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    msg = await channel.send(embed=embed)  # https://cog-creators.github.io/discord-embed-sandbox/
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")


@suggestions.error
async def suggestions_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="suggestions",
            description="To use the suggestions command just text what you what to suggest",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="suggestions `text or set`")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(error)
    else:
        print(F"Suggestion Error {error}")


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def request(ctx, *, message):
    with open("Files/Bot_Suggestions.json") as f:
        requests = json.load(f)
    try:
        requests[message] += 1
    except KeyError:
        requests[message] = 1
    with open("Files/Bot_Suggestions.json", "w") as f:
        json.dump(requests, f, indent=4)
    await ctx.send("your request has been sent")


@request.error
async def request_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Request",
            description="To use the request command just text what you what to suggest",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="request `text`")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(error)
    else:
        print(F"request Error {error}")

