import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import time
import json


version = 1.6

# Loads the discord server id to the .json file
def get_prefix(bot, message):
    with open("Files/Prefix.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=intents)
bot.remove_command("help")

