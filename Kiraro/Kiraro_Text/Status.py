import discord
from discord.ext import commands
from Kiraro.Kiraro_Text import is_us
from Kiraro import bot

@bot.command()
async def Change_Stream_Status(ctx, link, *, stream_name):
    if is_us(ctx.author.id):
        await bot.change_presence(activity=discord.Streaming(name=stream_name, url=link))
        await ctx.send(f"Stream status set to **{stream_name}** with the url set to **{link}**")


@Change_Stream_Status.error
async def Change_Stream_Status_error(ctx, error):
    if is_us(ctx.author.id):
        if isinstance(error, discord.HTTPException):
            await ctx.send("Something went wrong, try again later")
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="Change Stream Status",
                description="To use the Change_Stream_Status command add the stream link first then the stream title",
                color=discord.Color.blue()
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.add_field(name="Usage", value="Change_Stream_Status `<stream link>` `<stream name>`")
            await ctx.send(embed=embed)
        else:
            print(F"Change Stream Status Error {error}")


@bot.command()
async def Change_Listening_Status(ctx, act_name):
    if is_us(ctx.author.id):
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=act_name))
        await ctx.send(f"Listening status set to **{act_name}**")


@Change_Listening_Status.error
async def Change_Listening_Status_error(ctx, error):
    if is_us(ctx.author.id):
        if isinstance(error, discord.HTTPException):
            await ctx.send("Something went wrong, try again later")
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="Change listening Status",
                description="To use the Change_Listening_Status command look below",
                color=discord.Color.blue()
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.add_field(name="Usage", value="Change_Listening_Status `<listening to>`")
            await ctx.send(embed=embed)
        else:
            print(F"Change Listening Status Error {error}")


@bot.command()
async def Change_watching_status(ctx, act_name):
    if is_us(ctx.author.id):
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=act_name))
        await ctx.send(f"Watching status set to **{act_name}**")


@Change_watching_status.error
async def Change_watching_status_error(ctx, error):
    if is_us(ctx.author.id):
        if isinstance(error, discord.HTTPException):
            await ctx.send("Something went wrong, try again later")
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="Change_watching_status",
                description="To use the Change_watching_status command look below",
                color=discord.Color.blue()
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.add_field(name="Usage", value="Change_listening_Status `<Watching>`")
            await ctx.send(embed=embed)
        else:
            print(F"Change Watching Status Error {error}")


@bot.command()
async def online(ctx, act_name=None):
    if is_us(ctx.author.id):
        await bot.change_presence(status=discord.Status, activity=discord.Streaming(name="My Stream", url=act_name))
        await ctx.send("`Status is now set to Online`")


@bot.command()
async def offline(ctx):
    if is_us(ctx.author.id):
        await bot.change_presence(status=discord.Status.invisible,
                                  activity=discord.Streaming(name="My Stream", url="error"))
        await ctx.send("`Status is now set to Offline`")


@bot.command()
async def away(ctx):
    if is_us(ctx.author.id):
        await bot.change_presence(status=discord.Status.idle,
                                  activity=discord.Streaming(name="My Stream", url="error"))
        await ctx.send("`Status is now set to Away`")


@bot.command()
async def DND(ctx):
    if is_us(ctx.author.id):
        await bot.change_presence(status=discord.Status.do_not_disturb,
                                  activity=discord.Streaming(name="My Stream", url="error"))
        await ctx.send("`Status is now set to Do Not Disturb`")


@bot.command()
async def OnlineSet(ctx, *, act_name):
    if is_us(ctx.author.id):
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=act_name))
        await ctx.send(f"I have changed my status to `Online` with the activity `{act_name}`")


@OnlineSet.error
async def OnlineSet_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="OnlineSet",
            description="To use the OnlineSet command look below",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="OnlineSet `<Status>`")
        await ctx.send(embed=embed)
    else:
        print(F"OnlineSet Error {error}")


@bot.command()
async def DNDSet(ctx, *, act_name):
    if is_us(ctx.author.id):
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name=act_name))
        await ctx.send(f"I have changed my status to `Do Not Disturb` with the activity `{act_name}`")


@DNDSet.error
async def DNDSet_error(ctx, error):
    if is_us(ctx.author.id):
        if isinstance(error, discord.HTTPException):
            await ctx.send("Something went wrong, try again later")
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="DNDSet",
                description="To use the DNDSet command look below",
                color=discord.Color.blue()
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.add_field(name="Usage", value="DNDSet `<Status>`")
            await ctx.send(embed=embed)
        else:
            print(F"DNDSet Error {error}")


@bot.command()
async def AwaySet(ctx, *, act_name):
    if is_us(ctx.author.id):
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=act_name))
        await ctx.send(f"I have changed my status to `Away` with the activity `{act_name}`")


@AwaySet.error
async def AwaySet_error(ctx, error):
    if is_us(ctx.author.id):
        if isinstance(error, discord.HTTPException):
            await ctx.send("Something went wrong, try again later")
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="AwaySet",
                description="To use the AwaySet command look below",
                color=discord.Color.blue()
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.add_field(name="Usage", value="AwaySet `<Status>`")
            await ctx.send(embed=embed)
        else:
            print(F"AwaySet Error {error}")
