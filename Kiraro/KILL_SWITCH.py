from Kiraro import is_us, bot
import sys
import asyncio


@bot.command()
async def KILL(ctx):
    if is_us(ctx.author.mention):
        await ctx.send("Are you sure you what to kill the program? [y(es)/n(o)]")

        def check(m):
            return m.author == ctx.author

        try:
            msg = await bot.wait_for('message', check=check, timeout=20)

            if msg.content.lower() in ['y', 'yes']:
                await ctx.send("I am killing the program, this will be log")
                print(ctx.author, "Has stopped the program")
                sys.exit()
            elif msg.content.lower() in ['n', 'no']:
                await ctx.send("Not killing the program!")
            else:
                await ctx.send("Invalid answer")
        except asyncio.TimeoutError:
            await ctx.send("Looks like you waited to long.")
