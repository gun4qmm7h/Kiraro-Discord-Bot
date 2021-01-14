from Kiraro import bot
from discord.ext import commands
from discord.errors import *
from discord.utils import get
from Kiraro.Kiraro_Voice import idk, queue
import discord
import gtts

queue_list = {}

@bot.command()
async def say(ctx, *, word):
    boolean, voice = await idk(ctx)
    if boolean:
        tts = gtts.gTTS(word)
        tts.save("Voice_Files/TTS.wav")
        try:
            voice.play(discord.FFmpegPCMAudio("Voice_Files/TTS.wav")) #, after=lambda e: queue(ctx, queue_list, voice))
            voice.source = discord.PCMVolumeTransformer(voice.source)
        except ClientException:
            queue_list[ctx.guild.id].append(word)
            print(queue_list)


@say.error
async def say_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Say",
            description="To use the Say command just add the text",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="Say `message` ")
        await ctx.send(embed=embed)
    else:
        print(F"Say Error {error}")