import discord
from Kiraro.Kiraro_Text import is_us
from Kiraro import bot, version
import json
import os


@bot.command(aliases=['h'])
async def Help(ctx):
    embed = discord.Embed(
        title="Help",
        colour=discord.Colour.blue()
    )
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.add_field(name="__TextHelp__", value="`Show's Text Help Menu`", inline=True)
    embed.add_field(name="__VoiceHelp__", value="`Show's Voice Help Menu`", inline=True)
    embed.add_field(name="__Aliases__", value="`Show's Aliases Menu`", inline=False)
    embed.set_footer(text=F"Version {version}")
    await ctx.send(embed=embed)


@bot.command(aliases=['TxtHelp'])
async def TextHelp(ctx):
    embed = discord.Embed(
        title="Text Help Menu",
        colour=discord.Colour.blue()
    )
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.add_field(name="__Rank__", value="**Rank**: `Show users Text Rank`\n"
                                           "**VRank**: `Show users Voice Rank`\n"
                                           "**LeaderBoard**: `Shows top 10 Text/Voice Rank`\n"
                                           "**LiveLeaderBoard**: `Same as LeaderBoard but updates every 30 sec`\n"
                                           "**DeleteRank**: `Delete Text/Voice Rank`\n"
                                           "**StopRank**: `Stops Text/Voice Rank`\n"
                                           "**StartRank**: `Starts Text/Voice Rank`\n",
                    inline=False)
    embed.add_field(name="__Moderator__", value="**Kick**: `Kick's a user`\n"
                                                "**Ban**: `Ban's a user`\n"
                                                "**Warn**: `Warns a users`\n"
                                                "**Warnings**: `Shows a users warns`\n"
                                                "**Clear**: `Clears a message`\n"
                                                "**Mute**: `Mute's a users`\n"
                                                "**UnMute**: `UnMutes' a users`\n"
                                                "**Stats**: `Show's how many users are in a server`\n"
                                                "**GiveAway**: `Stats a GiveAway`\n"
                                                "**Prefix**: `Changes the Prefix`\n"
                                                "**Set**: `Can set welcome/leave/Suggest to a channel`\n"
                                                "**LockDown**: `Stop message being sent ot the channel`\n"
                                                "**Hide**: `Hide's a channel`\n"
                                                "**Send**: `Can send text to any channel`\n"
                                                "**DeleteWarnings**: `Deletes a users warnings`",
                    inline=False)
    embed.add_field(name="__Joke__", value="**Meme**: `Sends a random meme`\n"
                                           "**Nsfw**: `Sends porn`\n"
                                           "**Joke**: `Tell's you a joke`\n"
                                           "**Size**: `Tell's you your PP size`\n"
                                           "**Coin**: `Flips a coin`\n"
                                           "**GiveNum**: `Gives you a random number`\n",
                    inline=False)
    embed.set_footer(text=F"If You What To Send Us A Suggest Or Report A Bug To Us Type >Request"
                          F"\nVersion {version}")
    await ctx.send(embed=embed)


@bot.command(aliases=['VcHelp'])
async def VoiceHelp(ctx):
    embed = discord.Embed(
        title="Voice Help Menu (In Beta)",
        colour=discord.Colour.blue()
    )
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.add_field(name="__Joke__", value="**Say**: `Says what the users types`\n",
                    inline=False)
    embed.add_field(name="__Join/Leave__", value="**Join**: `Join a call and plays a cool noise`\n"
                                                 "**Leave**: `Leaves a call and plays a cool noise`\n",
                    inline=False)
    embed.set_footer(text=F"If You What To Send Us A Suggest Or Report A Bug To Us Type >Request"
                          F"\nVersion {version}")
    await ctx.send(embed=embed)


@bot.command()
async def aliases(ctx):
    embed = discord.Embed(
        title="Aliases menu",
        description=F"Instead of typing the full command we made it easy by using aliases ",
        color=discord.Color.blue())
    embed.add_field(name="__Aliases__", value="""
**Clear**: `delete, c`
**Delete_rank**: `del_rank, delrank, remove_rank`
**LiveLeaderboard**: `livelb, lb_live, live_lb`
**Leaderboard**: `lb, lboard`
**Lockdown**: `shutdown, ld, sd`
**MuteRole**: `muterole, mutedrole, mrole, muted_role`
**Mute**: `Timeout`
**VoiceRank**: `vc_rank, vrank, vc, voice`
**Suggestions**: `suggest, sug`
**Warnings**: `search, find, locate`
**DeleteWarnings**: ` del_warnings, delwarnings, remove_warnings`
**StartRank**: `Startr`
**StopRank**: `Stopr`
""")
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    await ctx.send(embed=embed)


@bot.command(aliases=["sh", "status"])
async def status_help(ctx):
    if await is_us(ctx.author.id):
        with open("Files/Prefix.json", "r") as f:
            prefixes = json.load(f)

        prefix = prefixes.get(str(ctx.guild.id))
        embed = discord.Embed(
            title="Help",
            description=F'''Type {prefix}<command> to get full information on how to use a command. 
```
{prefix}Onlineset <status>
{prefix}Awayset: <status>
{prefix}dndset: <status>
==========================================================
{prefix}Online
{prefix}Offline
{prefix}Away
{prefix}dnd
==========================================================
{prefix}Change_Stream_Status <stream url> <stream name>
{prefix}Change_listening_Status <title>
{prefix}Change_watching_status <title>
```
''',
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)


@bot.command(aliases=['changel', 'clogs', 'update'])
async def change_logs(ctx):
    embed = discord.Embed(
        title="Change Logs",
        description=F'''
added new commands [nsfw, meme, joke, hide, size]
can't kick, ban, mute user with admin
changing the help and aliases looks
''',
        color=discord.Color.blue())
    embed.set_footer(text=F"Version {version}")
    await ctx.send(embed=embed)
