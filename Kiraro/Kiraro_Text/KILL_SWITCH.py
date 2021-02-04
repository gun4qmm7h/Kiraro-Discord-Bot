from Kiraro.Kiraro_Text import is_us
from Kiraro import bot
import webbrowser
import sys
import asyncio
import discord



@bot.command()
async def KILL(ctx):
    if await is_us(ctx.author.id):
        print(ctx.author, "Has attempt to stopped the Bot")

        embed = discord.Embed(color=0xffdd00)
        embed.add_field(name="Kill bot",
                        value="This will shut down the bot are you sure you want to do this",
                        inline=False)
        embed.set_footer(text="type y(es) or n(o) to confirm or abort")
        await ctx.send(embed=embed)

        def check(m):
            return m.author == ctx.author

        try:
            msg = await bot.wait_for('message', check=check, timeout=20)

            if msg.content.lower() in ['y', 'yes']:
                embed = discord.Embed(color=0xff0000)
                embed.add_field(name="Kill command Successful",
                                value="Looks like I wasn't wanted anymore :( ",
                                inline=True)
                embed.add_field(name=":(",
                                value=f"Shutting down. Logging this command in Run log for you {ctx.author.name}",
                                inline=False)
                embed.set_footer(text="I wonder what I did wrong?")
                await ctx.send(embed=embed)

                print(ctx.author, "Has stopped the Bot")
                sys.exit()
            elif msg.content.lower() in ['n', 'no']:
                embed = discord.Embed(color=0x1eff00)
                embed.add_field(name="Kill command aborted",
                                value="Looks like I'm still wanted. Aborting shutdown.",
                                inline=False)
                embed.set_footer(text=f"Thank you {ctx.author.name}")
                await ctx.send(embed=embed)
            else:
                await ctx.send("Invalid answer")
        except asyncio.TimeoutError:
            embed = discord.Embed(color=0xffae00)
            embed.add_field(name="Kill command aborted",
                            value="You may not still want me but you took too long to answer so you gotta deal with me now.",
                            inline=True)
            embed.set_footer(text="you took too long so I will abort the command and stay on")
            await ctx.send(embed=embed)


# @bot.command()
# async def troll(ctx):
#     if is_us(ctx.author.id):
#         num = 0
#         while num <= 200:
#             webbrowser.open_new("")
#             num += 1
#