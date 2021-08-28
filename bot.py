import discord
import os
from discord import client
import discord.ext.commands
from dotenv import load_dotenv 
import json
import sqlite3 as sl
import random
## TRY TO FIX SQLITE OR FIND AN ALTERNATIVE
## E.G.: PARSING INTO .TXT
################## INITIATE ################################
conn = sl.connect("data.sqlite3")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS test (guild_id, test);""")
cur.execute("""CREATE TABLE IF NOT EXISTS user (userid, curr INTEGER);""")
load_dotenv()
bot = discord.ext.commands.Bot(command_prefix="..!")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name="Test mode initiated"))

############################################################

def testdata(conn, input):
    sql = "UPDATE test SET test = ? WHERE guild_id = ?"
    cur.execute(sql,input)
    conn.commit()

############################################################
## COMMAND:
# @bot.command()
# async def <COMMAND NAME>(ctx, <insert args>):
@bot.command()
async def user(ctx, arg):
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
@bot.command()
async def test2(ctx, arg):
    cur.execute("CREATE TABLE IF NOT EXISTS guild" + str(ctx.guild.id) + " (uid,curr)")
    cur.execute("SELECT * FROM guild"+str(ctx.guild.id)+" WHERE uid = "+str(ctx.author.id))
    res = cur.fetchone()
    try: (uid, cr) = res
    except:
        cur.execute("INSERT INTO guild"+str(ctx.guild.id)+" (uid,curr) VALUES (?, ?)",(ctx.author.id,arg))
        conn.commit()
    finally:
        cur.execute("UPDATE guild"+str(ctx.guild.id)+" SET curr = ? WHERE uid = ?",(arg, ctx.author.id))
@bot.command()
async def start(ctx):
    cur.execute("INSERT INTO test (guild_id) VALUES ("+str(ctx.guild.id)+")")
    conn.commit()
@bot.command()
async def test(ctx, arg): 
    cur.execute("SELECT * FROM test WHERE guild_id = " + str(ctx.guild.id))
    res = cur.fetchone()
    (gid, tst) = res
    await ctx.send(str(tst)+"-->"+str(arg))
    testdata(conn, (arg, ctx.guild.id))
@bot.command()
async def con(ctx):
    print("success")
@bot.command()
async def hug(ctx, arg):
    await ctx.send("<@"+str(ctx.author.id)+">" + " hugs " + arg)
@bot.command()
async def dice(ctx, arg):
    embedDice = discord.Embed(title="Dice", color =discord.Color.from_rgb(100, 255, 20))
    embedDice.add_field(name="You have rolled:", value=str(random.randint(1,int(arg))))
    await ctx.send(embed=embedDice)
@bot.command()
async def shutdown(ctx):
    if ctx.author.id == 472448933348769795:
        await ctx.send("Night night.")
        await bot.close()
    else:
        await ctx.send("YOU DON'T HAVE PERMISSION TO DO THAT :x:")
@bot.command()
async def goatfact(ctx):
    goatfacts = [
        "Goat revolution is near.", 
        "Goats exist.",
        "Goat goes 'baaaa'.", 
        "Scientists changed genomes of a goat to produce bulletproof vests from their milk.", 
        "Goats were one of the first animals to be tamed by humans and were being herded 9,000 years ago.",
        "Goat meat is the most consumed meat per capita worldwide."
        ]
    await ctx.send(random.choice(goatfacts))

###

@bot.command()
async def embed(ctx, arg1, arg2, cr, cb, cg):
    embedVar = discord.Embed(title=arg1, description=arg2, color=discord.Color.from_rgb(int(cr), int(cb), int(cg)))
    await ctx.send(embed=embedVar)

# help command, update regularly

@bot.command()
async def cmds(ctx):
    embedHelp = discord.Embed(title="Commands:", desc="Prefix = ..!", color =discord.Color.from_rgb(200, 255, 20))
    embedHelp.add_field(name="hug", value="Hugs a user \n Usage: `..!hug <target>`")
    embedHelp.add_field(name="embed", value="Sends an embed. \n Usage: `..!embed <title> <desc> <red> <blue> <green>`")
    embedHelp.add_field(name="goatfact", value="Facts about goats!")
    await ctx.send(embed=embedHelp)

bot.run(os.getenv('TOKEN'))