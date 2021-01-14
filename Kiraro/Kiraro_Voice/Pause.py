import discord
from Kiraro import bot


@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        await ctx.send("The song is pause")
    else:
        await ctx.send("No audio is playing")


@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_pause():
        voice.resume()
        await ctx.send("resuming the song")
    else:
        await ctx.send("the song is not pause")