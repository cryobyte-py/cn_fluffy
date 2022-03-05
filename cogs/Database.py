import requests
from requests.exceptions import HTTPError
import discord
import random
import sqlite3 as sl
from discord.ext import commands
conn = sl.connect('assets/data.sqlite3')
cur = conn.cursor()
class Database(commands.Cog, name='Database'):
    def __init__(self, bot):
        self.bot = bot
    def setup(bot):
        bot.add_cog(Utility(bot))
    @commands.command(help="//DEBUG//")
    async def user(self, ctx, arg):
        cur.execute("select * from user where userid =" + str(ctx.author.id))
        res = cur.fetchone()
        try: (uid,cr) = res
        except:
            cur.execute("INSERT INTO user (userid) VALUES (?, ?)",(ctx.author.id, arg))
            conn.commit()
        finally:
            cur.execute("UPDATE user SET curr = ? WHERE userid = ?",(arg, ctx.author.id))
            cur.fetchone()
            conn.commit()
            (uid,cr) = res
            await ctx.send(str(cr)+"--->"+str(arg))
    @commands.command(help="//DEBUG//")
    async def guild_reg(self, ctx, arg):
        cur.execute("CREATE TABLE IF NOT EXISTS guild" + str(ctx.guild.id) + " (uid,curr)")
        cur.execute("SELECT * FROM guild"+str(ctx.guild.id)+" WHERE uid = "+str(ctx.author.id))
        res = cur.fetchone()
        try: (uid, cr) = res
        except:
            cur.execute("INSERT INTO guild"+str(ctx.guild.id)+" (uid,curr) VALUES (?, ?)",(ctx.author.id,arg))
            conn.commit()
        finally:
            cur.execute("UPDATE guild"+str(ctx.guild.id)+" SET curr = ? WHERE uid = ?",(arg, ctx.author.id))
            conn.commit()
    @commands.command(help="//DEBUG//")
    async def start(self, ctx): 
        cur.execute("INSERT INTO guild (guild_id) VALUES ("+str(ctx.guild.id)+")")
        conn.commit()
    @commands.command()
    async def con(self, ctx):
        print("success")
