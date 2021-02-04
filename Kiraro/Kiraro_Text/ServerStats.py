import discord
from discord.ext import commands
from Kiraro import bot
import json


@bot.command()
@commands.has_permissions(administrator=True)
async def stats(ctx):
    category = await ctx.guild.create_category("📊 SERVER STATS 📊")
    channel = await category.create_voice_channel(F"All Members: {ctx.guild.member_count}")
    perms = channel.overwrites_for(ctx.guild.default_role)
    perms.connect = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=perms)
    with open("Files/Stats.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = channel.id

    with open("Files/Stats.json", "w") as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(
        f"`I have set up the stat counter at the top of all the channels. You are at {ctx.guild.member_count}"
        f" members, this will be updated accordingly`")


@stats.error
async def stats_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Giveaway Error",
            description="You are missing the **permission** `administrator`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print(F"Stats Error {error}")