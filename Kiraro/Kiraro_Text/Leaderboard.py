import discord
from discord.ext import commands
from Kiraro.Kiraro_Text import TextRank, VoiceRank
from Kiraro import bot
import json


@bot.command(aliases=['lb', 'lboard', 'levels'])
async def leaderboard(ctx, ranking, number: int = 10):
    if ranking.lower() in ["text", "txt", "t"]:

        msg, low_user, name_dir = await TextRank(ctx.guild.id, ctx, number=number)

        if low_user or len(name_dir) < 10:
            await ctx.send("I can't do top 10 because there isn't enough user ranked")

    elif ranking.lower() in ["voice", "vc", "v"]:

        msg, low_user, name_dir = await VoiceRank(ctx.guild.id, ctx, number=number)

        if low_user or len(name_dir) < 10:
            await ctx.send("I can't do top 10 because there isn't enough user ranked")


@leaderboard.error
async def leaderboard_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Leaderboard",
            description="To use the leaderboard command just say what rank you what to see",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="leaderboard `text or voice` `number`")
        await ctx.send(embed=embed)
    else:
        print(F"leaderboard Error {error}")


@bot.command(aliases=['livelb', 'lb_live', 'live_lb'])
async def live_Leaderboard(ctx, ranking, number: int = 10):
    if ranking.lower() in ["text", "txt", "t"]:

        message, low_user, name_dir = await TextRank(ctx.guild.id, ctx, live=True)

        if low_user or len(name_dir) < 10:
            await ctx.send("I can't do top 10 because there isn't enough user ranked")

        with open("Files/Live_Leaderboard.json") as f:
            livelb = json.load(f)

        server = livelb[str(ctx.guild.id)]
        server["text"] = True
        server["txt_message"] = []
        server["txt_message"].extend((ctx.channel.id, message.id, number))

        with open("Files/Live_Leaderboard.json", "w") as f:
            json.dump(livelb, f, indent=4)

    elif ranking.lower() in ["voice", "vc", "v"]:

        message, low_user, name_dir = await VoiceRank(ctx.guild.id, ctx, live=True)

        if low_user or len(name_dir) < 10:
            await ctx.send("I can't do top 10 because there isn't enough user ranked")

        with open("Files/Live_Leaderboard.json") as f:
            livelb = json.load(f)

        server = livelb[str(ctx.guild.id)]
        server["voice"] = True
        server["vc_message"] = []
        server["vc_message"].extend((ctx.channel.id, message.id, number))

        with open("Files/Live_Leaderboard.json", "w") as f:
            json.dump(livelb, f, indent=4)


@live_Leaderboard.error
async def live_Leaderboard_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="live_Leaderboard",
            description="To use the leaderboard command just say what rank you what to see",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="leaderboard `text or voice` `number`")
        await ctx.send(embed=embed)
    else:
        print(F"leaderboard Error {error}")

