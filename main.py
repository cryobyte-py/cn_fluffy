from re import I
from aiohttp import client
import discord
import os
import time
from discord.ext import commands
from dotenv import load_dotenv
import sqlite3 as sl
from cogs.Debug import Debug
from cogs.Moderation import Moderation
from cogs.Utility import Utility
from cogs.Social import Social
from cogs.Debug import conn, cur
load_dotenv()
token = os.getenv('TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "..!", intents = intents)
bot.add_cog(Social(bot))
bot.add_cog(Utility(bot))
bot.add_cog(Debug(bot))
bot.add_cog(Moderation(bot))
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print(bot.cogs)
bot.run(token)