"""
Author: Jawad
Version: 1.5
2020-01-14
fix some bugs and working on Kiraro voice
"""

import os
import importlib
from Kiraro import bot

remove_lst = ['__init__.py', '__pycache__']

dir_path_text = os.listdir("Kiraro/Kiraro_Text")
for files in dir_path_text:
    if files not in remove_lst:
        module = F"Kiraro.Kiraro_Text.{files[:-3]}"
        importlib.import_module(module)


dir_path_voice = os.listdir("Kiraro/Kiraro_Voice")
for files in dir_path_voice:
    if files not in remove_lst:
        module = F"Kiraro.Kiraro_Voice.{files[:-3]}"
        importlib.import_module(module)




# kiraro token
bot.run('Token')
NTc3MjMxMzgwMzkyNzA2MDQ5.XNiCnQ.toCHiUkzUjxthhN2u2smq2Z7R6Y
