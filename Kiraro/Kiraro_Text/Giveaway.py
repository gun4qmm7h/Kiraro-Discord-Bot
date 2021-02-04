import discord
from discord.ext import commands
from Kiraro.Kiraro_Text import get_sec
from Kiraro import bot
import random
import asyncio

@bot.command()
@commands.has_permissions(administrator=True)
async def giveaway(ctx, times, num_of_users, *, giveaway_msg=None):
    if int(num_of_users) == 0:
        await ctx.send("Really? :|")
        return
    embed = discord.Embed(color=0x006eff)
    embed.add_field(name="Giveaway", value=F"Started By: {ctx.author.mention}", inline=False)
    embed.add_field(name="Number Of Winners", value=num_of_users, inline=False)
    embed.add_field(name="Description", value=giveaway_msg, inline=False)
    embed.add_field(name="Time Left", value=times, inline=False)
    embed.set_footer(text="React to join the event")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("🎉")
    await asyncio.sleep(await get_sec(times))
    msg = await msg.channel.fetch_message(msg.id)
    people = []
    for reaction in msg.reactions:
        async for user in reaction.users():
            people.append(user.id)
    people.remove(bot.user.id)
    all_winners = []
    if len(people) == 0:
        await ctx.send("No one reacted to the giveaway :(")
    elif len(people) < int(num_of_users):
        people_num = len(people)
        for x in range(len(people)):
            winner = random.choice(people)
            all_winners.append(str(winner))
            people.remove(winner)
        await ctx.send(F"<@{', '.join(all_winners)}>, Not enough people reacted "
                       F"so the number will be off {people_num}/{num_of_users}")
    else:
        for x in range(int(num_of_users)):
            winner = random.choice(people)
            all_winners.append(str(winner))
            people.remove(winner)
        embed = discord.Embed(
            title="Winners",
            description=":drum: The Winners Are :drum: ",
            colour=discord.Colour.green()
        )
        embed.add_field(name="ㅤ", value=F"<@{', '.join(all_winners)}>")
        await ctx.send(embed=embed)


@giveaway.error
async def giveaway_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Giveaway Error",
            description="You are missing the **permission** `Administrator`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Giveaway",
            description="To use the Giveaway command just add the time and the message",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="Giveaway `time` `num of users` `message` ")
        await ctx.send(embed=embed)
    else:
        print(F"Giveaway Error {error}")