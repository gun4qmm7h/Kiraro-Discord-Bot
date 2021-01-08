from Kiraro import bot
from discord.utils import get
import discord
import gtts


@bot.command()
async def say(ctx, *, word):
    tts = gtts.gTTS(word)
    tts.save("Voice_Files/TTS.wav")
    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Voice_Files/TTS.wav"))
    voice.source = discord.PCMVolumeTransformer(voice.source)

@say.error
async def say_error(ctx, error):
    pass  # TODO