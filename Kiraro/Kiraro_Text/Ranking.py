import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from Kiraro.Kiraro_Text import human_format, get_hours, xp_background, circle
from Kiraro import bot
import json

@bot.command()
async def rank(ctx, user: discord.Member = None):
    with open("Files/Stop_Start_Rank.json") as f:
        stop_start = json.load(f)
    server = stop_start[str(ctx.guild.id)]
    if server["text"]:
        if not bool(user):
            user = ctx.author
        im1 = Image.open(xp_background)
        mask_im = Image.open("Images/mask_circle.jpg")
        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        im3 = Image.open(data)
        draw = ImageDraw.Draw(im1)

        rank_level = ImageFont.truetype('Files/Helios Regular.ttf', 53)
        font1 = ImageFont.truetype('Files/Helios Regular.ttf', 30)

        with open("Files/TextRanking.json") as f:
            rank = json.load(f)
        server = rank[str(ctx.guild.id)]
        users = server['users']

        name_dir = {}
        lst = []
        for x in users:
            if x['name'] == str(user.id):
                next_xp = x['next_xp']
                xp = x['xp']
                level = x['level']
            name_dir[x["message"]] = x['name']
            lst.append(x['message'])

        lst = sorted(lst, reverse=True)
        num = 1
        for i in lst:
            if str(name_dir[i]) == str(user.id):
                rank_num = num
                break
            num += 1

        full = 880
        percentage = xp / next_xp * 100
        if percentage < 6:
            percentage = 6

        coords = ((percentage / 100) * full, 230, 55, 230)
        W = 44
        COLOR = "#007FFF"
        name = str(user)
        text_size = draw.textsize(name, font=font1)

        draw.line(coords, width=W, fill=COLOR)
        await circle(draw, (coords[0], coords[1]), W / 2, COLOR)
        await circle(draw, (coords[2], coords[3]), W / 2, COLOR)

        score = F"{human_format(xp)}/{human_format(next_xp)}"
        rank_num = F'#{human_format(rank_num)}'
        level = human_format(level)

        text_w, text_h = draw.textsize(score, font=font1)
        draw.text((880 - text_w, 240 - text_h), score, (0, 0, 0), font=font1)

        rank_num_size = draw.textsize(rank_num, font=rank_level)
        level_size = draw.textsize(level, font=rank_level)
        im1_size = im1.size
        im3_size = im3.size

        draw.text((110 - (rank_num_size[0] / 2), 105 - (rank_num_size[1] / 2)), rank_num, (255, 255, 255), font=rank_level)
        draw.text((810 - (level_size[0] / 2), 105 - (level_size[1] / 2)), level, (255, 255, 255), font=rank_level)
        draw.text((round(im1_size[0] / 2 - text_size[0] / 2), round(im1_size[1] / 2 - text_size[1] / 2 + 50)), name,
                  (255, 255, 255), font=font1)

        im3 = im3.resize((140, 140))
        im1.paste(im3, (round(im1_size[0] / 2 - im3_size[0] / 2), round(im1_size[1] / 2 - im3_size[0] / 2 - 45)), mask_im)
        im1.save("Images/Rank.png", quality=100)
        await ctx.send(file=discord.File("Images/Rank.png"))


@rank.error
async def rank_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Seems like I can't find that user")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("That user does not have a rank")
    else:
        print(F"Text Rank Error {error}")


@bot.command(aliases=['vc_rank', 'vrank', 'vc', 'voice'])
async def VoiceRank(ctx, user: discord.Member = None):
    with open("Files/Stop_Start_Rank.json") as f:
        stop_start = json.load(f)
    server = stop_start[str(ctx.guild.id)]
    if server["voice"]:
        if not bool(user):
            user = ctx.author
        im1 = Image.open(xp_background)
        mask_im = Image.open("Images/mask_circle.jpg")
        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        im3 = Image.open(data)
        draw = ImageDraw.Draw(im1)

        rank_level = ImageFont.truetype('Files/Helios Regular.ttf', 53)
        font1 = ImageFont.truetype('Files/Helios Regular.ttf', 30)

        with open("Files/VoiceRanking.json") as f:
            Voice = json.load(f)

        server = Voice[str(ctx.guild.id)]
        users = server['users']
        for x in users:
            if x['name'] == str(user.id):
                level = x['hours']
                xp = round(x['time_sec'])
                next_xp = level + 1

        name_dir = {}
        lst = []
        for x in users:
            name_dir[x['seconds']] = x['name']
            lst.append(x['seconds'])

        lst = sorted(lst, reverse=True)

        num = 1
        for i in lst:
            if name_dir[i] == str(user.id):
                rank_num = num
                break
            num += 1

        next_xp *= 3600

        percentage = (xp / next_xp) * 100

        if percentage < 6:
            percentage = 6

        full = 880
        coords = ((percentage / 100) * full, 230, 55, 230)
        W = 44
        COLOR = "#007FFF"
        name = str(user)
        text_size = draw.textsize(name, font=font1)

        draw.line(coords, width=W, fill=COLOR)
        await circle(draw, (coords[0], coords[1]), W / 2, COLOR)
        await circle(draw, (coords[2], coords[3]), W / 2, COLOR)

        score = F"{get_hours(xp)}/{get_hours(next_xp)}"
        rank_num = F'#{human_format(rank_num)}'
        level = human_format(level)

        text_w, text_h = draw.textsize(score, font=font1)
        draw.text((880 - text_w, 240 - text_h), score, (0, 0, 0), font=font1)
        im3 = im3.resize((140, 140))

        rank_num_size = draw.textsize(rank_num, font=rank_level)
        level_size = draw.textsize(level, font=rank_level)
        im1_size = im1.size
        im3_size = im3.size

        draw.text((110 - (rank_num_size[0] / 2), 105 - (rank_num_size[1] / 2)), rank_num, (255, 255, 255), font=rank_level)
        draw.text((810 - (level_size[0] / 2), 105 - (level_size[1] / 2)), level, (255, 255, 255), font=rank_level)

        draw.text((round(im1_size[0] / 2 - text_size[0] / 2), round(im1_size[1] / 2 - text_size[1] / 2 + 50)), name,
                  (255, 255, 255), font=font1)

        im1.paste(im3, (round(im1_size[0] / 2 - im3_size[0] / 2), round(im1_size[1] / 2 - im3_size[0] / 2 - 45)), mask_im)
        im1.save("Images/Rank.png", quality=100)
        await ctx.send(file=discord.File("Images/Rank.png"))


@VoiceRank.error
async def VoiceRank_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Seems like I can't find that user")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("That user does not have a rank")
    else:
        print(F"Voice Rank Error {error}")


@bot.command(aliases=['Stopr'])
@commands.has_permissions(administrator=True)
async def StopRank(ctx, string):
    if string.lower() in ["text", "txt", "t"]:
        with open("Files/Stop_Start_Rank.json") as f:
            stop_start = json.load(f)

        server = stop_start[str(ctx.guild.id)]
        server.update({"text": False})

        with open("Files/Stop_Start_Rank.json", "w") as f:
            json.dump(stop_start, f, indent=4)
        await ctx.send("The Text ranking will be stopped")
    elif string.lower() in ["voice", "vc", "v"]:
        with open("Files/Stop_Start_Rank.json") as f:
            stop_start = json.load(f)

        server = stop_start[str(ctx.guild.id)]
        server.update({"voice": False})

        with open("Files/Stop_Start_Rank.json", "w") as f:
            json.dump(stop_start, f, indent=4)
        await ctx.send("The Voice ranking will be stopped")


@StopRank.error
async def StopRank_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Stop Error",
            description="You are missing the **permission** `administrator`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Stop",
            description="To use the Stop command just add text or voice",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="Stop `text or voice`")
        await ctx.send(embed=embed)
    else:
        print(F"Stop_Rank Error {error}")


@bot.command(aliases=['Startr'])
@commands.has_permissions(administrator=True)
async def StartRank(ctx, string):
    if string.lower() in ["text", "txt", "t"]:
        with open("Files/Stop_Start_Rank.json") as f:
            stop_start = json.load(f)

        server = stop_start[str(ctx.guild.id)]
        server.update({"text": True})

        with open("Files/Stop_Start_Rank.json", "w") as f:
            json.dump(stop_start, f, indent=4)
        await ctx.send("The Text ranking will Start")

    elif string.lower() in ["voice", "vc" "v"]:
        with open("Files/Stop_Start_Rank.json") as f:
            stop_start = json.load(f)

        server = stop_start[str(ctx.guild.id)]
        server.update({"voice": True})

        with open("Files/Stop_Start_Rank.json", "w") as f:
            json.dump(stop_start, f, indent=4)
        await ctx.send("The Voice ranking will Start")

@StartRank.error
async def StartRank_error(ctx, error):
    if isinstance(error, discord.HTTPException):
        await ctx.send("Something went wrong, try again later")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Start Error",
            description="You are missing the **permission** `administrator`",
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Start",
            description="To use the Start command just add text or voice",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usage", value="Start `text or voice`")
        await ctx.send(embed=embed)
    else:
        print(F"Stop_Rank Error {error}")