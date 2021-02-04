"""
Author: Jawad, Jake
Version: 1.5
2020-01-14
fix some bugs and working on Kiraro voice
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
bot.run('Token')
