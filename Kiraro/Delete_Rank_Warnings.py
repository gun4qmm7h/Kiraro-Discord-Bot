import discord
from discord.ext import commands
from Kiraro import bot, hash_lib
import json
import asyncio


@bot.command(aliases=['del_rank', 'delrank', 'remove_rank'])
@commands.has_permissions(administrator=True)
async def delete_rank(ctx, ranking):
    if ranking.lower() in ["text", "txt", "t"]:
        await ctx.send("Are you sure you what to delete text rank? [y(es)/n(o)]")

        def check(m):
            return m.author == ctx.author

        try:
            msg = await bot.wait_for('message', check=check, timeout=20)

            if msg.content.lower() in ['y', 'yes']:
                with open("Files/TextRanking.json") as f:
                    text = json.load(f)
                text.pop(str(ctx.guild.id))
                with open("Files/TextRanking.json", "w") as f:
                    json.dump(text, f, indent=4)
                await ctx.send("Text rank removed")
            elif msg.content.lower() in ['n', 'no']:
                await ctx.send("Not delete the text rank")
            else:
                await ctx.send("I did not understand that, aborting!")
        except asyncio.TimeoutError:
            await ctx.send("Looks like you waited to long.")


    elif ranking.lower() in ["voice", "vc", "v"]:
        await ctx.send("Are you sure you what to delete voice rank? [y(es)/n(o)]")

        try:
            msg = await bot.wait_for('message', check=check, timeout=20)

            if msg.content.lower() in ['y', 'yes']:
                with open("Files/VoiceRanking.json") as f:
                    text = json.load(f)
                text.pop(str(ctx.guild.id))
                with open("Files/VoiceRanking.json", "w") as f:
                    json.dump(text, f, indent=4)
                await ctx.send("Voice rank removed")
            elif msg.content.lower() in ['n', 'no']:
                await ctx.send("Not removing the voice rank!")
            else:
                await ctx.send("I did not understand that, aborting!")
        except asyncio.TimeoutError:
            await ctx.send("Looks like you waited to long.")




@delete_rank.error
async def delete_rank_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Delete Rank Error",
            description="You are missing the **permission** `administrator`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Delete Rank",
            description="To use the delete_rank command just say what rank you what to delete",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="delete_rank `text or voice`")
        await ctx.send(embed=embed)
    else:
        print(F"Delete Rank Error {error}")


@bot.command(aliases=['del_warnings', 'delwarnings', 'remove_warnings'])
@commands.has_permissions(ban_members=True, kick_members=True)
async def delete_warnings(ctx, user: discord.Member, *, reason: int = None):
    with open("Files/warning.json") as f:
        report = json.load(f)
    server = report[str(ctx.guild.id)]
    for x in server['users']:
        if x["name"] == hash_lib(str(user.mention)):
            x["reasons"].pop(reason-1)
            x["times"] -= 1
            with open("Files/warning.json", "w") as f:
                json.dump(report, f, indent=4)
            await ctx.send(
                f"I have remove {user.mention} warning, time: {x['times']}, reasons: {', '.join(x['reasons'])}")


@delete_warnings.error
async def delete_warnings_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Delete Warnings Error",
            description="You are missing the **permission** `ban_members` `kick_member`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Seems like I can't find that user")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Delete Warnings",
            description="To use the delete_warnings command just add the user and what number you what to remove",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="delete_warnings `user` `number`")
        await ctx.send(embed=embed)
    else:
        print(F"Clear Warnings {error}")