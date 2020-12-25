import discord
from discord.ext import commands
from Kiraro import bot
import json


@bot.command()
@commands.has_permissions(manage_channels=True)
async def set(ctx, channel):
    if channel.lower() == "welcome" or channel.lower() == "join":
        with open("Files/join_leave.json") as f:
            join = json.load(f)

        try:
            server = join[str(ctx.guild.id)]
            server.update({"welcome": ctx.channel.id})
        except KeyError:
            join[ctx.guild.id] = {}
            server = join[ctx.guild.id]
            server.update({"welcome": ctx.channel.id})

        with open("Files/join_leave.json", "w") as f:
            json.dump(join, f, indent=4)
        await ctx.send(F"{ctx.channel} has been set as the welcome channel")
    elif channel.lower() == "goodbye" or channel.lower() == "leave":
        with open("Files/join_leave.json") as f:
            leave = json.load(f)

            try:
                server = leave[str(ctx.guild.id)]
                server.update({"goodbye": ctx.channel.id})
            except KeyError:
                leave[ctx.guild.id] = {}
                server = leave[ctx.guild.id]
                server.update({"goodbye": ctx.channel.id})

        with open("Files/join_leave.json", "w") as f:
            json.dump(leave, f, indent=4)
        await ctx.send(F"{ctx.channel} has been set as the goodbye channel")
    elif channel.lower() == "suggestions" or channel.lower() == "sug" or channel.lower() == "suggestion":
        with open("Files/Suggestions.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = ctx.channel.id

        with open("Files/Suggestions.json", "w") as f:
            json.dump(prefixes, f, indent=4)
        await ctx.send(F"{ctx.channel} is the suggestions channel")

@set.error
async def set_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Set Error",
            description="You are missing the **permission** `manage channel`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Seems like I can't find that user")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Set",
            description="To use the Set command just add the welcome or goodbye or suggestions",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="Set `welcome or goodbye or suggestions`")
        await ctx.send(embed=embed)
    else:
        print(F"Set Error {error}")