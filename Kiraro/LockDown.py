from Kiraro import bot
from discord.ext import commands
import discord

@bot.command(aliases=['shutdown', 'ld', 'sd'])
@commands.has_permissions(administrator=True)
async def lockdown(ctx):
    ow = ctx.channel.overwrites_for(ctx.guild.default_role)
    if ow.send_messages:
        perms = ctx.channel.overwrites_for(ctx.guild.default_role)
        perms.send_messages = False
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=perms)
        await ctx.send("The channel has been locked :) use the command again to unlock")
    else:
        perms = ctx.channel.overwrites_for(ctx.guild.default_role)
        perms.send_messages = True
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=perms)
        await ctx.send("The channel has been unlocked :)")


@lockdown.error
async def lockdown_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Role Error",
            description="You are missing the **permission** `Administrator`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print(F"lockdown Error {error}")