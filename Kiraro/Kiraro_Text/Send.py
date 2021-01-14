import discord
from Kiraro import bot
from discord.ext import commands


@bot.command()
@commands.has_permissions(manage_messages=True)
async def send(ctx, channel: discord.TextChannel, *, word):
    channel = bot.get_channel(channel.id)
    await channel.send(word)


@send.error
async def send_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Send",
            description="To use the send command just add the text",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="Send `channel` `message` ")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Send Error",
            description="You are missing the **permission** `Manage Channels`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print(F"lockdown Error {error}")
