import discord
from discord.ext import commands
from Kiraro import bot
import json

# Changes the prefix to a custom one
@bot.command()
@commands.has_permissions(administrator=True)
async def prefix(ctx, user_prefix):
    with open("Files/Prefix.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = user_prefix

    with open("Files/Prefix.json", "w") as f:
        json.dump(prefixes, f, indent=4)
    embed = discord.Embed(
        title="Prefix",
        description=F"Prefix has been change to \"{user_prefix}\"",
        color=discord.Color.blue()
    )
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@prefix.error
async def prefix_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Prefix Error",
            description="You are missing the **Permission** `Administrator`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        with open("Files/Prefix.json", "r") as f:
            prefixes = json.load(f)

        prefix = prefixes.get(str(ctx.guild.id))
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="Prefix",
                description=F"To use the Prefix command add your prefix after typing {prefix}Prefix",
                color=discord.Color.blue()
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.add_field(name="Usage", value="prefix `prefix`")
            await ctx.send(embed=embed)
        else:
            print(F"prefix Error {error}")