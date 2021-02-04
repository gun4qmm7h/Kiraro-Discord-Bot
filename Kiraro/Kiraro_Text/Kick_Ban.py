import discord
from discord.ext import commands
from Kiraro.Kiraro_Text import get_sec
from Kiraro import bot
import asyncio


# Ban users and checks if user has a ban_members role
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
    if user.guild_permissions.administrator:
        raise is_admin
    else:
        await user.ban(reason=reason)
        embed = discord.Embed(
            title="Ban",
            description=f"{user.mention} have been banned successfully",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Reason", value=reason)
        await ctx.send(embed=embed)

# Handles the errors from the ban command
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Ban Error",
            description="You are missing the **Permission** `Ban Members`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Seems like I can't find that user")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Ban",
            description="To use the ban command add the user name and a reason why they are getting baned",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="Ban `member` `reason`")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandInvokeError):
        embed = discord.Embed(
            description=F"""The user you trying to ban has a role higher then me

        To fix this go to `Server Setting>Roles` and move *{bot.user.name}* role
        higher then the role you are trying to ban.""",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, is_admin):
        embed = discord.Embed(
            title="",
            description="You can't ban an `Administrator`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print(F"Ban Error {error}")



@bot.command()
@commands.has_permissions(ban_members=True)
async def tempban(ctx, user: discord.Member, time, *, reason=None):
    if user.guild_permissions.administrator:
        raise is_admin
    else:
        await user.ban(reason=reason)
        embed = discord.Embed(
            title="TempBan",
            description=f"{user.mention} have been banned successfully for {time}",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Reason", value=reason)
        await ctx.send(embed=embed)
        await asyncio.sleep(get_sec(time))
        await user.unban()


# Handles the errors from the ban command
@tempban.error
async def tempban_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="TempBan Error",
            description="You are missing the **Permission** `Ban Members`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Seems like I can't find that user")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="TempBan",
            description="To use the TempBan command add the user name, time and a reason why they are getting baned",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="TempBan `member` `time` `reason`")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandInvokeError):
        embed = discord.Embed(
            description=F"""The user you trying to ban has a role higher then me

        To fix this go to `Server Setting>Roles` and move *{bot.user.name}* role
        higher then the role you are trying to ban.""",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, is_admin):
        embed = discord.Embed(
            title="",
            description="You can't ban an `Administrator`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print(F"TempBan Error {error}")




# kick users and checks if user has a kick_members role
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
    if user.guild_permissions.administrator:
        raise is_admin
    else:
        await user.kick(reason=reason)
        embed = discord.Embed(
            title="Kick",
            description=f"{user.mention} have been kick successfully",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Reason", value=reason)
        await ctx.send(embed=embed)


# Handles the errors from the kick command
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Kick Error",
            description="You are missing the **permission** `Kick Members`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Seems like I can't find that user")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Kick",
            description="To use the kick command add the user name and a reason why they are getting kicked",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="Kick `members` `reason`")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandInvokeError):
        embed = discord.Embed(
            description=F"""The user you trying to kick has a role higher then me

        To fix this go to `Server Setting>Roles` and move *{bot.user.name}* role
        higher then the role you are trying to kick.""",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, is_admin):
        embed = discord.Embed(
            title="",
            description="You can't kick an `Administrator`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print(F"Kick Error {error}")
