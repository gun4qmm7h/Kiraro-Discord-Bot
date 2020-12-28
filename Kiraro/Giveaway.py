import discord
from discord.ext import commands
from Kiraro import bot, get_sec
import random
import asyncio

@bot.command()
@commands.has_permissions(administrator=True)
async def giveaway(ctx, times, num_of_users, *, giveaway_msg=None):
    if int(num_of_users) == 0:
        await ctx.send("Really? :|")
        return
    embed = discord.Embed(color=0x006eff)
    embed.add_field(name="Giveaway", value=F"Started by: {ctx.author.mention}", inline=True)
    embed.add_field(name="Description", value=giveaway_msg, inline=False)
    embed.add_field(name="Number of winners", value=num_of_users, inline=False)
    embed.add_field(name="Time Left", value=times, inline=True)
    embed.set_footer(text="React to join the event")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("🎉")
    await asyncio.sleep(get_sec(times))
    msg = await msg.channel.fetch_message(msg.id)
    people = []
    for reaction in msg.reactions:
        async for user in reaction.users():
            people.append(user.mention)
    people.remove(bot.user.mention)
    all_winners = []
    if len(people) == 0:
        await ctx.send("No one reacted to the giveaway :(")
    elif len(people) < int(num_of_users):
        people_num = len(people)
        for x in range(len(people)):
            winner = random.choice(people)
            all_winners.append(winner)
            people.remove(winner)
        await ctx.send(F"{', '.join(all_winners)}, Not enough people reacted so the number will be off {people_num}/{num_of_users}")
    else:
        for x in range(int(num_of_users)):
            winner = random.choice(people)
            all_winners.append(winner)
            people.remove(winner)
        await ctx.send(F":drum: The winners are :drum: {', '.join(all_winners)}")


@giveaway.error
async def giveaway_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Giveaway Error",
            description="You are missing the **permission** `administrator`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Giveaway",
            description="To use the Giveaway command just add the time in %%d:%%h:%%m:%%s format and the message",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="Giveaway `time` `num of users` `message` ")
        await ctx.send(embed=embed)
    else:
        print(F"Giveaway Error {error}")