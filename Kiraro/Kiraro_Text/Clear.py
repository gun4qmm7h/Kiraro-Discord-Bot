import discord
from discord.ext import commands
from Kiraro import bot
import asyncio

# Clears the messages
@bot.command(aliases=['delete', 'c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount):
    if amount.lower() == "all":
        await ctx.channel.purge(limit=None)
        msg = await ctx.send("All message has been deleted.")
        await asyncio.sleep(1)
        await msg.delete()
    elif amount == "0":
        await ctx.send("Deleting 0 message because you know, that's possible ")
    else:
        await ctx.channel.purge(limit=int(amount) + 1)
        msg = await ctx.send(F"`{amount}` message has been deleted.")
        await asyncio.sleep(1)
        await msg.delete()


# Handles the errors from the clear command
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Clear Error",
            description="You are missing the **Permission** `Manage Messages`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("The arguments you enter contains letters")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Clear",
            description=F"To use the clear command type clear and the number of message you what to clear.",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="clear `number or all`")
        await ctx.send(embed=embed)
    else:
        print(F"Clear Error {error}")
#
