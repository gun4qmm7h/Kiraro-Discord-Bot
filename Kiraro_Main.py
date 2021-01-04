"""
Author: Jawad
Version: 1.2
2020-12-30
Big Change:
fix lockdown not working the first time
fix warnings throwing an error when no one on server was warned

Small Change:
made a variable for the xp_background
made the text/voice rank more usable for other commands and not just for updating the leaderboard
the kill_switch prints out when a user attempts to kill the bot
change the name of the xp background
In status i named the url error so it's more understandable that it's meant to make an error.
Move the circle func to __init__ file
rename .mention to .id because .mention will sometimes have a ! in it
make a folder for voice commands (in working progress)
importing is different. didn't what 20 lines of imports
added a troll command to use on my friend
"""


import os
import importlib
from Kiraro import bot

dir_path_text = os.listdir("Kiraro/Kiraro_Text")
for files in dir_path_text:
    if files not in ['__init__.py', '__pycache__']:
        module = F"Kiraro.Kiraro_Text.{files[:-3]}"
        importlib.import_module(module)


dir_path_voice = os.listdir("Kiraro/Kiraro_Voice")
for files in dir_path_voice:
    if files not in ['__init__.py', '__pycache__']:
        module = F"Kiraro.Kiraro_Voice.{files[:-3]}"
        importlib.import_module(module)




# kiraro token
bot.run('Token')