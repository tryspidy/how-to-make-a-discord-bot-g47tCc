#________________________________________________________________________________________#
#                                                                                        #
#                               How to make a discord bot                                #
#________________________________________________________________________________________#


# BE AWARE! YOU NEED TO CUSTOMIZE/CONFIGURE THIS CODE OTHERWISE IT WON'T WORK. 
# THIS CODE IS JUST THE BASICS



# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord

# IMPORTS EXTENSIONS FOR COMMANDS
from discord.ext import commands


# IMPORT THE OS MODULE.
import os

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

# IMPORT LOGGING

import logging


# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


bot = commands.Bot(command_prefix='Yourprefix')

# UNDER THIS LINE OF CODE ARE THE COMMANDS FOR THE BOT. YOU CAN ADD/CHANGE THOSE SAFELY WITHOUT DESTORYING THE CODE

@bot.command()
async def test(ctx, *, arg):
	await ctx.send(arg, file=discord.File('yourfile.png'))


@bot.command()
async def laugh(ctx):
	await ctx.send("typeherealink")




@bot.command()
async def die(ctx):
	exit()



# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. DON'T REMOVE THIS LINE OF CODE JUST CHANGE THE "DISCORD_TOKEN" PART TO YOUR DISCORD BOT TOKEN
bot.run(DISCORD_TOKEN)

#________________________________________________________________________________________#

# If this code helped you please leave a like on it. If you want to see more of this follow me
# Or just take a look at another answer of my answers
#
# THIS CODE HAS BEEN MADE BY : Vast Vicuña