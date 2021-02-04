from Kiraro import bot
from discord.utils import get
import gtts
import discord
import asyncio


# voice.source.volume = 0.60

@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    Join_Sound = "Voice_Files/Join_sound.wav"
    voice.play(discord.FFmpegPCMAudio(Join_Sound))
    voice.source = discord.PCMVolumeTransformer(voice.source)

    await ctx.send(f"Joined {channel}")

@bot.command()
async def leave(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        Leave_Sound = "Voice_Files/Leave_Sound.wav"
        voice.play(discord.FFmpegPCMAudio(Leave_Sound))
        await asyncio.sleep(1)
        await voice.disconnect()
        await ctx.send(f"Left {ctx.message.author.voice.channel}")
    else:
        await ctx.send("Don't think I am in a voice channel")


