import discord
import config
import random
from discord.ext import commands

####--------------------- INITIALIZE VARIABLES --------------------------####
token = config.token
description = "basic bot"
bot = commands.Bot(command_prefix='!', description=description)
commandList={"!hello":"replyes with a hello message (or not).",\
            "!kick":"kicks a member.",\
            "!commands": "prints a list of the existing bot commands.",\
            "!choose": "given an enumeration separated by 'or' random selects one of the options." }

####--------------------- EVENTS --------------------------####
@bot.event
async def on_ready():
    print("name: " + bot.user.name)
    print("id: " + bot.user.id)

####--------------------- BOT COMMANDS --------------------------####

@bot.command()
async def kick(member: discord.Member):
    await bot.kick(member)

@bot.command()
async def hello():
    try:
        await bot.say('Fuck you!')
    except Exception as e:
        return e

@bot.command()
async def commands():
    try:
        coms = '**Commands List**\n'
        for com in commandList:
            coms += '**{}** : {}\n'.format(com, commandList[com])
        await bot.say(coms)
    except Exception as e:
        return e

# !choose a or b; a,b or c;

@bot.command()
async def choose(*args):
    try:
        options = list(args)
        options = list(filter(lambda a: a != "or", options))
        chosen = random.choice(options)
        await bot.say('Hmmm, lets see...\nI choose: **{}**'.format(chosen))
    except Exception as e:
        return e
####--------------------- RUN --------------------------####
bot.run(token)