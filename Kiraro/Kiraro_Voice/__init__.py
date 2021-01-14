from Kiraro import bot
from discord.utils import get
import discord
import gtts


async def idk(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if ctx.author.voice is None:
        await ctx.send("You are not in a voice channel")
    if voice is None:
        channel = ctx.message.author.voice.channel
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
    if ctx.author.voice.channel.id != voice.channel.id:
        await ctx.send("I am being use in a another channel")
        return False
    return True, voice


def queue(ctx, queue_list, voice):
    while len(queue_list) != 0:
        queue_list = queue_list[ctx.guild.id]
        print(queue_list)
        tts = gtts.gTTS(queue_list[0])
        queue_list.pop(0)
        print(queue_list)
        tts.save("Voice_Files/TTS.wav")
        voice.play(discord.FFmpegPCMAudio("Voice_Files/TTS.wav"), after=lambda e: queue(ctx, queue_list, voice))
        voice.source = discord.PCMVolumeTransformer(voice.source)