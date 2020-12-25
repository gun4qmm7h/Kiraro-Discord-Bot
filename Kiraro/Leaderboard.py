import discord
from discord.ext import commands
from Kiraro import bot, get_days
import json


@bot.command(aliases=['lb', 'lboard'])
async def leaderboard(ctx, ranking, number: int = 10):
    if ranking.lower() in ["text", "txt", "t"]:
        with open("Files/TextRanking.json", "r") as f:
            rank = json.load(f)
        server = rank[str(ctx.guild.id)]
        users = server['users']
        name_dir = {}
        msg_num = []
        for x in users:
            name_dir[x["message"]] = [x['name'], x['xp'], x['level'], x['next_xp']]
            msg_num.append(x['message'])

        msg_num = sorted(msg_num, reverse=True)

        num = 1
        low_user = False
        embed = discord.Embed(title="Text Rank Leaderboard", color=0x006eff)
        for i in msg_num:
            user_id = ''.join([i for i in name_dir[i][0] if i.isdigit()])
            user_name = bot.get_user(int(user_id))

            if user_name is None:
                low_user = True
                break

            embed.add_field(name=F"#{num}: {user_name}",
                            value=F"***Xp***: {name_dir[i][1]}\n"
                                  F"***Next Xp***: {name_dir[i][3]}\n"
                                  F"***Level***: {name_dir[i][2]}\n"
                                  F"***Message***: {i}",
                            inline=False)
            if number == num:
                break
            num += 1
        await ctx.send(embed=embed)
        if low_user or len(name_dir) < 10:
            await ctx.send("I can't do top 10 because there isn't enough user rank")

    elif ranking.lower() in ["voice", "vc", "v"]:
        with open("Files/VoiceRanking.json") as f:
            voice = json.load(f)
        name_dir = {}
        sec = []
        server = voice[str(ctx.guild.id)]
        user = server['users']
        for x in user:
            name_dir[x["time_sec"]] = [x['name']]
            sec.append(x['time_sec'])

        sec = sorted(sec, reverse=True)

        num = 1
        low_user = False
        embed = discord.Embed(title="Voice Rank Leaderboard", color=0x006eff)
        for i in sec:
            user_id = ''.join([i for i in name_dir[i][0] if i.isdigit()])
            user_name = bot.get_user(int(user_id))

            if user_name is None:
                low_user = True
                break

            embed.add_field(name=F"#{num}: {user_name}", value=F"***Time***: {get_days(round(i))}", inline=False)
            if number == num:
                break
            num += 1
        await ctx.send(embed=embed)
        if low_user or len(name_dir) < 10:
            await ctx.send("I can't do top 10 because there isn't enough user")


@leaderboard.error
async def leaderboard_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Leaderboard",
            description="To use the leaderboard command just say what rank you what to see",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="leaderboard `text or voice` `number`")
        await ctx.send(embed=embed)
    else:
        print(F"leaderboard Error {error}")


@bot.command(aliases=['livelb', 'lb_live', 'live_lb'])
async def live_Leaderboard(ctx, ranking, number: int = 10):
    if ranking.lower() in ["text", "txt", "t"]:
        with open("Files/TextRanking.json", "r") as f:
            rank = json.load(f)
        server = rank[str(ctx.guild.id)]
        users = server['users']
        name_dir = {}
        msg_num = []
        for x in users:
            name_dir[x["message"]] = [x['name'], x['xp'], x['level'], x['next_xp']]
            msg_num.append(x['message'])

        msg_num = sorted(msg_num, reverse=True)

        num = 1
        low_user = False
        embed = discord.Embed(title="Text Rank Live Leaderboard", color=0x006eff)
        for i in msg_num:
            user_id = ''.join([i for i in name_dir[i][0] if i.isdigit()])
            user_name = bot.get_user(int(user_id))

            if user_name is None:
                low_user = True
                break

            embed.add_field(name=F"#{num}: {user_name}",
                            value=F"***Xp***: {name_dir[i][1]}\n"
                                  F"***Next Xp***: {name_dir[i][3]}\n"
                                  F"***Level***: {name_dir[i][2]}\n"
                                  F"***Message***: {i}",
                            inline=False)

            if num == number:
                break
            num += 1
        embed.set_footer(text="This leaderboard will be updated every 30 seconds")
        message = await ctx.send(embed=embed)
        if low_user or len(name_dir) < 10:
            await ctx.send("I can't do top 10 because there isn't enough user")

        with open("Files/Live_Leaderboard.json") as f:
            livelb = json.load(f)

        server = livelb[str(ctx.guild.id)]
        server["text"] = True
        server["txt_message"] = []
        server["txt_message"].extend((ctx.channel.id, message.id, number))

        with open("Files/Live_Leaderboard.json", "w") as f:
            json.dump(livelb, f, indent=4)

    elif ranking.lower() == ["voice", "vc", "v"]:
        with open("Files/VoiceRanking.json") as f:
            voice = json.load(f)
        name_dir = {}
        sec = []
        server = voice[str(ctx.guild.id)]
        user = server['users']
        for x in user:
            name_dir[x["time_sec"]] = [x['name']]
            sec.append(x['time_sec'])

        sec = sorted(sec, reverse=True)

        num = 1
        low_user = False
        embed = discord.Embed(title="Voice Rank Leaderboard", color=0x006eff)
        for i in sec:
            user_id = ''.join([i for i in name_dir[i][0] if i.isdigit()])
            user_name = bot.get_user(int(user_id))

            if user_name is None:
                low_user = True
                break

            embed.add_field(name=F"#{num}: {user_name}", value=F"***Time***: {get_days(round(i))}", inline=False)

            if num == number:
                break
            num += 1
        embed.set_footer(text="This leaderboard will be updated every 30 seconds")
        message = await ctx.send(embed=embed)
        if low_user or len(name_dir) < 10:
            await ctx.send("I can't do top 10 because there isn't enough user")

        with open("Files/Live_Leaderboard.json") as f:
            livelb = json.load(f)

        server = livelb[str(ctx.guild.id)]
        server["voice"] = True
        server["vc_message"] = []
        server["vc_message"].extend((ctx.channel.id, message.id, number))

        with open("Files/Live_Leaderboard.json", "w") as f:
            json.dump(livelb, f, indent=4)


@live_Leaderboard.error
async def live_Leaderboard_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="live_Leaderboard",
            description="To use the leaderboard command just say what rank you what to see",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="leaderboard `text or voice` `number`")
        await ctx.send(embed=embed)
    else:
        print(F"leaderboard Error {error}")

