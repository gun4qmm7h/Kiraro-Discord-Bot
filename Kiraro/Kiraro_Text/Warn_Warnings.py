import discord
from discord.ext import commands
from Kiraro import bot
import json


@bot.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, user: discord.Member, *, reason=None):
    with open("Files/warning.json") as f:
        report = json.load(f)
    server = report.get(str(ctx.guild.id))
    if server is not None:
        new_user = True
        for person in server['users']:
            if person["name"] == str(user.id):
                person['reasons'].append(str(reason))
                person['times'] += 1
                new_user = False
                break
        if new_user:
            server['users'].append({
                'name': str(user.id),
                'reasons': [str(reason)],
                'times': 1
            })
    if server is None:
        report[str(ctx.guild.id)] = {"users": []}
        server = report[str(ctx.guild.id)]
        server['users'].append({
            'name': str(user.id),
            'reasons': [str(reason)],
            'times': 1
        })
    with open("Files/warning.json", "w") as f:
        json.dump(report, f, indent=4)
    report = report[str(ctx.guild.id)]
    report = report['users']
    for x in report:
        if x['name'] == str(user.id):
            try:
                embed = discord.Embed(color=0x00b3ff)
                embed.add_field(name=F"You have been warned in {ctx.guild}", value=F"Reason: {reason}", inline=False)
                embed.add_field(name="Warning #", value=x['times'], inline=True)
                await user.send(embed=embed)

                embed = discord.Embed(title=" ", color=0x006eff)
                embed.set_author(name=F"{ctx.author.name}", icon_url=ctx.author.avatar_url)
                embed.add_field(name="Warn", value=F"I have warned {user.mention} ", inline=False)
                embed.add_field(name="Reason", value=reason, inline=True)
                embed.add_field(name="Warning #", value=x['times'], inline=False)
                await ctx.send(embed=embed)
                break
            except discord.errors.Forbidden:
                embed = discord.Embed(title=" ", color=discord.Color.red())
                embed.set_author(name=F"{ctx.author.name}", icon_url=ctx.author.avatar_url)
                embed.add_field(name="Not Warn", value=F"I Could not warn {user.mention} ", inline=False)
                await ctx.send(embed=embed)
                break


@warn.error
async def warn_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Warn Error",
            description="You are missing the **permission** `Administrator`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Seems like I can't find that user")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Warn",
            description="To use the Warn command add the user name and a reason why they are getting warned",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="warn `members` `reason`")
        await ctx.send(embed=embed)
    else:
        print(F"Warn Error {error}")


@bot.command(aliases=['search', 'find', 'locate'])
@commands.has_permissions(administrator=True)
async def warnings(ctx, user: discord.Member):
    with open("Files/warning.json", "r") as f:
        report = json.load(f)
    if not bool(report.get(str(ctx.guild.id))) or report.get(str(ctx.guild.id)) is None:
        await ctx.send(f"{user.mention} has never been reported")
        return
    report = report[str(ctx.guild.id)]
    new_user = True
    for current_user in report['users']:
        if str(user.id) == current_user['name']:
            embed = discord.Embed(title=" ", color=0x006eff)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            for x in range(current_user['times']):
                embed.add_field(name=F"Warn {x + 1}", value=F"warned for {current_user['reasons'][x]}", inline=False)
            await ctx.send(embed=embed)
            new_user = False
            break
    if new_user:
        await ctx.send(f"{user.mention} has never been reported")


@warnings.error
async def warnings_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Warning Error",
            description="You are missing the **permission** `Administrator`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Seems like I can't find that user")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Warnings",
            description="To use the Warnings command just add the users name",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="warnings `members`")
        await ctx.send(embed=embed)
    else:
        print(F"Warnings Error {error}")