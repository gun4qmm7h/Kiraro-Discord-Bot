import discord
from discord.ext import commands
from Kiraro.Kiraro_Text import hash_lib
from Kiraro import bot
import json
import asyncio



@bot.command(aliases=['del_rank', 'delrank', 'remove_rank'])
@commands.has_permissions(administrator=True)
async def delete_rank(ctx, ranking):

    def check(m):
        return m.author == ctx.author

    if ranking.lower() in ["text", "txt", "t"]:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name="Delete Text Ranks",
                        value="Are you sure you want to delete the text ranks. Once you do this there is no going back.",
                        inline=False)
        embed.set_footer(text="Type yes to delete all text ranks, type no to abort.")
        await ctx.send(embed=embed)

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
                embed = discord.Embed(color=0x04ff00)
                embed.add_field(name="Delete Text Ranks Successful", value="All Text ranks have been deleted",
                                inline=False)
                embed.set_footer(text=f"{ctx.author.name} has deleted all text ranks")
                await ctx.send(embed=embed)

            elif msg.content.lower() in ['n', 'no']:
                await ctx.send("Not delete the text rank")
            else:
                await ctx.send("I did not understand that, aborting!")
        except asyncio.TimeoutError:
            await ctx.send("Looks like you waited to long.")


    elif ranking.lower() in ["voice", "vc", "v"]:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name="Delete Voice Ranks",
                        value="Are you sure you want to delete the voice ranks. Once you do this there is no going back",
                        inline=False)
        embed.set_footer(text="Type yes to delete all voice ranks, type no to abort.")
        await ctx.send(embed=embed)

        try:
            msg = await bot.wait_for('message', check=check, timeout=20)

            if msg.content.lower() in ['y', 'yes']:
                with open("Files/VoiceRanking.json") as f:
                    text = json.load(f)
                text.pop(str(ctx.guild.id))
                with open("Files/VoiceRanking.json", "w") as f:
                    json.dump(text, f, indent=4)
                embed = discord.Embed(color=0x04ff00)
                embed.add_field(name="Delete Voice Ranks Successful", value="All voice ranks have been deleted",
                                inline=False)
                embed.set_footer(text=f"{ctx.author.name} has deleted all voice ranks")
                await ctx.send(embed=embed)

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
async def delete_warnings(ctx, user: discord.Member, reason: int = None):

    def check(m):
        return m.author == ctx.author

    with open("Files/warning.json") as f:
        report = json.load(f)
    if not bool(report.get(str(ctx.guild.id))) or report.get(str(ctx.guild.id)) is None:
        return
    server = report[str(ctx.guild.id)]
    for x in server['users']:
        if x["name"] == await hash_lib(str(user.id)):
            break

    embed = discord.Embed(color=0xff0000)
    embed.add_field(name="Delete Warnings",
                    value=F"Are you sure you want to remove {user.mention} warning",
                    inline=False)
    embed.add_field(name="**Warnings**", value=F"Reasons: {x['reasons'][reason-1]} ")
    embed.set_footer(text=F"Type yes to delete {user.name} warnings, type no to abort.")
    await ctx.send(embed=embed)

    try:
        msg = await bot.wait_for('message', check=check, timeout=20)

        if msg.content.lower() in ['y', 'yes']:

            embed = discord.Embed(color=0xff0000)
            embed.add_field(name="Delete Warnings Successful",
                            value="The warnings have been deleted",
                            inline=False)
            embed.add_field(name="**Warnings**", value=F"Reasons: {x['reasons'][reason - 1]} \n"
                                                       F"Times: {x['times']}")
            embed.set_footer(text=f"{ctx.author.name} has deleted {user.name} warnings")
            await ctx.send(embed=embed)
            x["reasons"].pop(reason-1)
            x["times"] -= 1
            with open("Files/warning.json", "w") as f:
                json.dump(report, f, indent=4)

        elif msg.content.lower() in ['n', 'no']:
            await ctx.send(F"Not deleting {user.mention} warnings")
        else:
            await ctx.send("I did not understand that, aborting!")
    except asyncio.TimeoutError:
        await ctx.send("Looks like you waited to long.")




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