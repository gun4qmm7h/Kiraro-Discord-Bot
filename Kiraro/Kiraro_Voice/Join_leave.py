from Kiraro import bot
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import discord


@bot.command()
async def join(ctx):
    voice = ctx.message.author.voice.channel
    await voice.connect()

@bot.command()
async def leave(ctx):
    voice = ctx.message.author.voice.channel
    await voice.disconnect()
    # await self.bot.get_guild(int(guild_id)).leave()