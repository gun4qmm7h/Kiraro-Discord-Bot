"""
Author: Jawad, Jake
Version: 1.6
2021-02-04
remove hash from warnings (thought it might cuz error with new features)
added an embed for the user getting warned
made a ping command
made a user command that tell you about user information
made some jokes command (e.x. meme, nsfw, joke, size, coin, givenum, urban, _8ball)
made a poll command and a send command that sends embeds to a channel
"""

import os
import importlib
from Kiraro.Error import *
from Kiraro.Help import *
from Kiraro import bot

remove_lst = ['__init__.py', '__pycache__']

for files in os.listdir("Kiraro/Kiraro_Text"):
    if files not in remove_lst:
        module = F"Kiraro.Kiraro_Text.{files[:-3]}"
        importlib.import_module(module)


for files in os.listdir("Kiraro/Kiraro_Voice"):
    if files not in remove_lst:
        module = F"Kiraro.Kiraro_Voice.{files[:-3]}"
        importlib.import_module(module)


# Kiraro token
bot.run('TOKEN')
