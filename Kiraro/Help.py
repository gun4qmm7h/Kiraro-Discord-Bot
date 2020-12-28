import discord
from discord.ext import commands
from Kiraro import bot, is_us, version
import json


@bot.command(aliases=['h'])
async def help(ctx):
    with open("Files/Prefix.json", "r") as f:
        prefixes = json.load(f)

    prefix = prefixes.get(str(ctx.guild.id))
    embed = discord.Embed(
        title="Help",
        description=F'''Type {prefix}<command> to get full information on how to use a command. 
    ```
{prefix}Help: Show's you a list of commands
{prefix}Kick: Kicks members
{prefix}Ban: Ban members
{prefix}Clear: Clears messages
{prefix}Warn: Warns a user
{prefix}Warnings: Shows a users warnings
{prefix}Stats: Server status
{prefix}Giveaway: starts a giveaway
{prefix}Prefix: Changes the Prefix
{prefix}Delete_Rank: Deletes all ranking levels and XP
{prefix}Leaderboard: Shows the leaderboard for either text or voice
{prefix}Mute: Mutes a user
{prefix}Unmute: Unmute's a user
{prefix}Rank: Shows the rank of a user
{prefix}Set: Sets the welcome, leave, or suggestion channel
{prefix}Suggest: Sends a suggestion to the suggestion channel
{prefix}Mute_role: Makes a role for muting, type mute_role to update the newer new channels
{prefix}Lockdown: Locks a channel so people cant type
{prefix}Live_Leaderboard: Posts a live leaderboard of the server
{prefix}Stop_Rank: Stop the text and voice ranking
{prefix}Start_Rank: Start the text and voice ranking
{prefix}Aliases: Show aliases for commands
```
if you what to send us a Suggest or report a bug to us type >request
Version {version}
''',
        color=discord.Color.blue())
    await ctx.send(embed=embed)


@bot.command()
async def aliases(ctx):
    with open("Files/Prefix.json", "r") as f:
        prefixes = json.load(f)

    prefix = prefixes.get(str(ctx.guild.id))
    embed = discord.Embed(
        title="Alias menu",
        description=F'''Instead of typing the full command we made it easy by using aliases 
```
{prefix}Clear= delete, c
{prefix}Delete_rank= del_rank, delrank, remove_rank
{prefix}Help= h
{prefix}live_Leaderboard= livelb, lb_live, live_lb
{prefix}leaderboard= lb, lboard
{prefix}lockdown= shutdown, ld, sd
{prefix}mute_role= muterole, mutedrole, mrole, muted_role
{prefix}mute= Timeout
{prefix}voice_rank= vc_rank, vrank, vc, voice
{prefix}suggestions= suggest, sug
{prefix}warnings= search, find, locate
{prefix}start_rank= Startr
{prefix}stop_rank= Stopr
```
''',
        color=discord.Color.blue())
    await ctx.send(embed=embed)


@bot.command()
async def status_help(ctx):
    if is_us(ctx.author.mention):
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
    Added a cool down to text ranking so a user only gets xp per text after 5 sec
    Added a Change Log command (This)
    Fix the text and voice ranking so they are more reliable
    ***Version {version}***
    ''',
        color=discord.Color.blue())
    await ctx.send(embed=embed)