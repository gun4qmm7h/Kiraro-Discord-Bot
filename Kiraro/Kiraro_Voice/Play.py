from Kiraro import bot
from discord.utils import get
import discord
import youtube_dl


@bot.command()
async def play(ctx, *, music: str):
    pass
    # voice = get(bot.voice_clients, guild=ctx.guild)
    # voice.play(discord.FFmpegPCMAudio("Voice_Files/Troll.webm"))
    # voice.source = discord.PCMVolumeTransformer(voice.source)
    # TODO