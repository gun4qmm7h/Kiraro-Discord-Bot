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


@bot.command(pass_context=True)
async def poll(ctx):
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    await ctx.send("whats the question?")
    question = await bot.wait_for("message", check=check)

    done = False
    num = 1
    message_list = []
    reaction = []
    while not done:
        await ctx.send(F"Whats Is Option {num}?")
        message_list.append(await bot.wait_for("message", check=check))
        await ctx.send(F"What Reaction Do You Want Opinions {num} To Have")
        reaction.append(await bot.wait_for("message", check=check))
        num += 1
        await ctx.send("Are You Done? yes or no")
        msg = await bot.wait_for("message", check=check)
        if msg.content in ["yes", "ye", "y"]:
            done = True

    embed = discord.Embed(
        title=question.content,
        color=discord.Color.blue()
    )
    x = 0
    for word in message_list:
        embed.add_field(name=str(x+1), value=F"{reaction[x].content} = {word.content}", inline=False)
        x += 1

    message_poll = await ctx.send(embed=embed)
    for x in reaction:
        await message_poll.add_reaction(x.content)


