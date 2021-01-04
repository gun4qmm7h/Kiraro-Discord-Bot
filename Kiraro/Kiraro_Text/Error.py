from discord.ext import commands
from Kiraro import bot
import json

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        """
        If an unknown command is enter, it will be saved in a file so we know what command to add
        next or what aliases to add
        """
        with open("Files/Command_Error.json") as f:
            command = json.load(f)
        error = (str(error).split(" ")[1]).strip('"')
        try:
            command[error] += 1
        except KeyError:
            command[error] = 1
        with open("Files/Command_Error.json", "w") as f:
            json.dump(command, f, indent=4)
    elif isinstance(error, commands.MissingRequiredArgument):
        pass
    elif isinstance(error, commands.MissingPermissions):
        pass
    else:
        print(F"on_command_error {error}")