import discord
from discord.ext import commands
from Kiraro import bot
from Kiraro.Kiraro_Text import get_sec
import json
import asyncio


@bot.command(aliases=['muterole', 'mutedrole', 'mrole', 'muted_role'])
@commands.has_permissions(manage_messages=True)
async def mute_role(ctx, name=None, role_color=discord.Color.default()):
    try:
        with open("Files/Mute.json") as f:
            Mute = json.load(f)
        role = Mute[str(ctx.guild.id)]
        await ctx.send("Updating the channels")
        for roles in ctx.guild.roles:
            if roles.id == role:
                break
        num = 0
        for channel in ctx.guild.channels:
            ow = channel.overwrites_for(roles)
            if ow.send_messages is None and ow.speak is None:
                if str(channel.type) == "text":
                    perms = channel.overwrites_for(roles)
                    perms.send_messages = False
                    await channel.set_permissions(roles, overwrite=perms)
                    num += 1
                elif str(channel.type) == "voice":
                    perms = channel.overwrites_for(roles)
                    perms.speak = False
                    await channel.set_permissions(roles, overwrite=perms)
                    num += 1
        await ctx.send(F"I have updated {num} channels")
    except KeyError:
        await ctx.send("Give me some time to make the role")
        if not bool(name):
            raise commands.BadArgument
        roles = await ctx.guild.create_role(name=name, color=role_color)
        for channel in ctx.guild.channels:
            if str(channel.type) == "text":
                perms = channel.overwrites_for(roles)
                perms.send_messages = False
                await channel.set_permissions(roles, overwrite=perms)
            elif str(channel.type) == "voice":
                perms = channel.overwrites_for(roles)
                perms.speak = False
                await channel.set_permissions(roles, overwrite=perms)
        with open("Files/Mute.json") as f:
            Mute = json.load(f)
        Mute[str(ctx.guild.id)] = roles.id
        with open("Files/Mute.json", "w") as f:
            json.dump(Mute, f, indent=4)
        await ctx.send(F"The role `{name}` has been created")


@mute_role.error
async def mute_role_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Role Error",
            description="You are missing the **permission** `Manage Messages`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Seems like we don't have that color or you didn't enter a name")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Role",
            description="To use the Role command just add a name and color",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="Role `name` `color`")
        await ctx.send(embed=embed)
    else:
        print(F"mute Error {error}")


@bot.command(aliases=['Timeout'])
@commands.has_permissions(manage_messages=True)
async def mute(ctx, user: discord.Member, time_mute=None):
    with open("Files/Mute.json") as f:
        Mute = json.load(f)
    Mute = Mute.get(str(ctx.guild.id))
    has_mute = False
    for roles in ctx.guild.roles:
        if roles.id == Mute:
            has_mute = True
            break

    if not has_mute:
        await ctx.send("mute role is not set. To set it use the command `mute_role`")
    else:
        await user.add_roles(roles)
        embed = discord.Embed(title="User Muted!", description=F"**{user.mention}** was muted by **{ctx.author.mention}**!",
                              color=discord.Color.blue())
        if bool(time_mute) and get_sec(time_mute):
            embed.add_field(name="Time", value=F"{user} will be unmuted in {time_mute}")
            await ctx.send(embed=embed)
            await asyncio.sleep(get_sec(time_mute))
            await user.remove_roles(roles)
        else:
            await ctx.send(embed=embed)


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Mute Error",
            description="You are missing the **permission** `Manage Messages`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Seems like I can't find that user")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Mute",
            description="To use the Mute command just add the users name and how long you what them muted for",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="mute `members` `time`")
        await ctx.send(embed=embed)
    else:
        print(F"mute Error {error}")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, user: discord.Member):
    with open("Files/Mute.json") as f:
        role_mute = json.load(f)
    try:
        Mute = role_mute[str(ctx.guild.id)]
        for roles in ctx.guild.roles:
            if roles.id == Mute:
                break

        if roles in user.roles:
            await user.remove_roles(roles)
            embed = discord.Embed(title=" ", color=0x006eff)
            embed.set_author(name=F"{ctx.author.name}", icon_url=ctx.author.avatar_url)
            embed.add_field(name="User Unmuted", value=F"{user.mention  } was unmuted by {ctx.author.mention}", inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=" ", color=0x006eff)
            embed.set_author(name=F"{ctx.author.name}", icon_url=ctx.author.avatar_url)
            embed.add_field(name="User Is Not Muted", value=F"{user} Is not muted", inline=False)
            await ctx.send(embed=embed)
    except KeyError:
        await ctx.send("You did not make a role, use the command `Mute_role`")


@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="UnMute Error",
            description="You are missing the **permission** `Manage Messages`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Seems like I can't find that user")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="UnMute",
            description="To use the UnMute command just add the users name to unmute them",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="unmute `members`")
        await ctx.send(embed=embed)
    else:
        print(F"Un-Mute Error {error}")
