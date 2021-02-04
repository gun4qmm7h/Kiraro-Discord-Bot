import discord
from Kiraro import bot


@bot.command()
async def ping(ctx):
    embed = discord.Embed(
        description=F"Bot latency is `{round(bot.latency * 1000)}ms`",
        colour=discord.Colour.blue()
    )
    await ctx.send(embed=embed)