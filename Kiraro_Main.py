"""
Author: Jawad
Version: 1.1
2020-12-26
Added cooldown to the ranking but in a way so the cooldown is not in effect if you ping the bot
Added a cooldown funcion to the __init__.py file
auto add server id's to files when added to servers
Kiraro discord bot
"""

from Kiraro.Clear import *
from Kiraro.Delete_Rank_Warnings import *
from Kiraro.Error import *
from Kiraro.Event import *
from Kiraro.EventRanking import *
from Kiraro.Event_Join_Leave import *
from Kiraro.Giveaway import *
from Kiraro.Help import *
from Kiraro.Kick_Ban import *
from Kiraro.Leaderboard import *
from Kiraro.Mute_UnMute import *
from Kiraro.Prefix import *
from Kiraro.Ranking import *
from Kiraro.ServerStats import *
from Kiraro.Set import *
from Kiraro.Status import *
from Kiraro.Suggestion import *
from Kiraro.Warn_Warnings import *
from Kiraro.KILL_SWITCH import *
from Kiraro.LockDown import *

from Kiraro import bot

import discord
from discord.ext import commands



# kiraro token
bot.run('Token')
