from logging import error
import discord
import os
from discord import client
from discord import player
from discord import message
import discord.ext.commands
from discord.ext import commands 
from discord import FFmpegPCMAudio
from dotenv import load_dotenv 
import json
import sqlite3 as sl
import random
import requests
from requests.exceptions import HTTPError
from discord.ext.commands import MissingPermissions, has_permissions
from discord.utils import get
## TRY TO FIX SQLITE OR FIND AN ALTERNATIVE
## E.G.: PARSING INTO .TXT
################## INITIATE ################################
conn = sl.connect("data.sqlite3")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS guild (guild_id PRIMARY KEY, mute_id, test);""")
cur.execute("""CREATE TABLE IF NOT EXISTS user (userid PRIMARY KEY, curr INTEGER);""")
load_dotenv()
bot = discord.ext.commands.Bot(command_prefix="..!")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name="with a portal gun! || Aperture Laboratories proudly presents"))
@bot.event
async def on_member_join(member):
    await member.send("Welcome!")
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permissions! :angry:")
    else:
        await ctx.send(f"`{error}`")
############################################################

def testdata(conn, input):
    sql = "UPDATE guild SET guild = ? WHERE guild_id = ?"
    cur.execute(sql,input)
    conn.commit()

############################################################
## COMMAND:
# @bot.command()
# async def <COMMAND NAME>(ctx, <insert args>):

### TODO: REFINE MUTE
#@bot.command(help="//DEBUG//")
#async def roletest(ctx, target: discord.Member):
#    if ctx.message.author.guild_permissions.administrator:
#        mut = get(ctx.guild.roles, name = "Muted")
#        await target.add_roles(mut)
#@bot.command(help="//DEBUG//")
#async def rolereturn(ctx):
#    mut = get(ctx.guild.roles, name = "Muted")
#    print(mut)
#    if mut is None:
#        print("Role not defined.")
#        perms = discord.Permissions(send_messages=False, read_messages=True)
#        await ctx.guild.create_role(name="Muted",perms=perms)
#    await ctx.send(f"Mute ID:{mut}")
@bot.command(help="Kicks the user")
async def kick(ctx, target: discord.Member, reason=None):
    await target.kick(reason=reason)
    await ctx.send(f"{target} had been kicked. Reason: {reason}")
@bot.command(help="Bans the user")
async def ban(ctx, target: discord.Member, reason=None):
    await target.ban(reason=reason)
    await ctx.send(f"{target} had been banned. Reason: {reason}")
@bot.command(help="//DEBUG//")
async def join(context):
        if (context.author.voice):
            channel = context.author.voice.channel
            voice = await channel.connect()
            player = voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="testaud.mp3"))
        else:
            context.send("You must be in a voice channel")
# Leave command, leaves the voice channel
@bot.command(help="//DEBUG//")
async def leave(context):
        await context.voice_client.disconnect()
@bot.command(help="//DEBUG//")
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
@bot.command(help="//DEBUG//")
async def guild_reg(ctx, arg):
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
@bot.command(help="//DEBUG//")
async def start(ctx): 
    cur.execute("INSERT INTO guild (guild_id) VALUES ("+str(ctx.guild.id)+")")
    conn.commit()
@bot.command()
async def con(ctx):
    print("success")
###text format test###
@bot.command(help="//DEBUG//")
async def format(ctx,user: discord.User):
    await ctx.send("`{0} test ".format(ctx.author)+user.name+ "`")
##### Social commands
@bot.command(help="Hugs a user")
async def hug(ctx, user: discord.User):
    try:
        response = requests.get('http://api.nekos.fun:8080/api/hug')
        response.raise_for_status()
        x = response.json()
        img = x["image"]
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    socialEmbed = discord.Embed(title="{0} hugs ".format(ctx.author)+user.name,color = discord.Color.from_rgb(100,240,20))
    socialEmbed.set_image(url=img)
    await ctx.send(embed=socialEmbed)
@bot.command(help="Kisses a user")
async def kiss(ctx, user: discord.User):
    try:
        response = requests.get('http://api.nekos.fun:8080/api/kiss')
        response.raise_for_status()
        x = response.json()
        img = x["image"]
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    socialEmbed = discord.Embed(title="{0} kisses ".format(ctx.author)+user.name,color = discord.Color.from_rgb(100,240,20))
    socialEmbed.set_image(url=img)
    await ctx.send(embed=socialEmbed)
@bot.command(help="Pats a user")
async def pat(ctx, user: discord.User):
    try:
        response = requests.get('http://api.nekos.fun:8080/api/pat')
        response.raise_for_status()
        x = response.json()
        img = x["image"]
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    socialEmbed = discord.Embed(title="{0} pats ".format(ctx.author)+user.name,color = discord.Color.from_rgb(100,240,20))
    socialEmbed.set_image(url=img)
    await ctx.send(embed=socialEmbed)
@bot.command(help="Cuddles a user")
async def cuddle(ctx, user: discord.User):
    try:
        response = requests.get('http://api.nekos.fun:8080/api/cuddle')
        response.raise_for_status()
        x = response.json()
        img = x["image"]
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    socialEmbed = discord.Embed(title="{0} cuddles ".format(ctx.author)+user.name+">^<",color = discord.Color.from_rgb(100,240,20))
    socialEmbed.set_image(url=img)
    await ctx.send(embed=socialEmbed)
@bot.command(help="Tickles a user")
async def tickle(ctx, user: discord.User):
    try:
        response = requests.get('http://api.nekos.fun:8080/api/tickle')
        response.raise_for_status()
        x = response.json()
        img = x["image"]
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    socialEmbed = discord.Embed(title="{0} tickles ".format(ctx.author)+user.name,color = discord.Color.from_rgb(100,240,20))
    socialEmbed.set_image(url=img)
    await ctx.send(embed=socialEmbed)
@bot.command(help="Pokes a user")
async def poke(ctx, user: discord.User):
    try:
        response = requests.get('http://api.nekos.fun:8080/api/poke')
        response.raise_for_status()
        x = response.json()
        img = x["image"]
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    socialEmbed = discord.Embed(title="{0} pokes ".format(ctx.author)+user.name,color = discord.Color.from_rgb(100,240,20))
    socialEmbed.set_image(url=img)
    await ctx.send(embed=socialEmbed)
@bot.command(help="Slaps a user")
async def slap(ctx, user: discord.User):
    try:
        response = requests.get('http://api.nekos.fun:8080/api/slap')
        response.raise_for_status()
        x = response.json()
        img = x["image"]
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    socialEmbed = discord.Embed(title="{0} slaps ".format(ctx.author)+user.name+" Ouch-",color = discord.Color.from_rgb(100,240,20))
    socialEmbed.set_image(url=img)
    await ctx.send(embed=socialEmbed)
@bot.command(help="Feeds a user")
async def feed(ctx, user: discord.User):
    try:
        response = requests.get('http://api.nekos.fun:8080/api/feed')
        response.raise_for_status()
        x = response.json()
        img = x["image"]
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    socialEmbed = discord.Embed(title="{0} feeds ".format(ctx.author)+user.name,color = discord.Color.from_rgb(100,240,20))
    socialEmbed.set_image(url=img)
    await ctx.send(embed=socialEmbed)
@bot.command(help="Licks a user")
async def lick(ctx, user: discord.User):
    try:
        response = requests.get('http://api.nekos.fun:8080/api/lick')
        response.raise_for_status()
        x = response.json()
        img = x["image"]
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    socialEmbed = discord.Embed(title="{0} licks ".format(ctx.author)+user.name,color = discord.Color.from_rgb(100,240,20))
    socialEmbed.set_image(url=img)
    await ctx.send(embed=socialEmbed)
@bot.command(help="Smug :3")
async def smug(ctx):
    try:
        response = requests.get('http://api.nekos.fun:8080/api/smug')
        response.raise_for_status()
        x = response.json()
        img = x["image"]
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    socialEmbed = discord.Embed(title="{0} is smirking ".format(ctx.author),color = discord.Color.from_rgb(100,240,20))
    socialEmbed.set_image(url=img)
    await ctx.send(embed=socialEmbed)
@bot.command(help="Cry ;w;")
async def cry(ctx):
    try:
        response = requests.get('http://api.nekos.fun:8080/api/cry')
        response.raise_for_status()
        x = response.json()
        img = x["image"]
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    socialEmbed = discord.Embed(title="{0} is crying ;-; ".format(ctx.author),color = discord.Color.from_rgb(100,240,20))
    socialEmbed.set_image(url=img)
    await ctx.send(embed=socialEmbed)
@bot.command(help="hahahaha :D")
async def laugh(ctx):
    try:
        response = requests.get('http://api.nekos.fun:8080/api/laugh')
        response.raise_for_status()
        x = response.json()
        img = x["image"]
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    socialEmbed = discord.Embed(title="{0} is laughing :D ".format(ctx.author),color = discord.Color.from_rgb(100,240,20))
    socialEmbed.set_image(url=img)
    await ctx.send(embed=socialEmbed)
#####
@bot.command(help="Rolls a dice")
async def dice(ctx, arg):
    embedDice = discord.Embed(title="Dice", color =discord.Color.from_rgb(100, 255, 20))
    embedDice.add_field(name="You have rolled:", value=str(random.randint(1,int(arg))))
    await ctx.send(embed=embedDice)
@bot.command(help="Remote shutdown - Developer Only")
async def shutdown(ctx):
    if ctx.author.id == 472448933348769795:
        await ctx.send("Night night.")
        await bot.close()
    else:
        await ctx.send("YOU DON'T HAVE PERMISSION TO DO THAT :x:")
@bot.command(help="Sends a cute fox")
async def fox(ctx):
    r = requests.get("https://randomfox.ca/floof/")
    foo = r.text
    foo = foo.split('"')[3]
    foo = foo.split("/")[4]
    await ctx.send("https://randomfox.ca/images/" + foo)
@bot.command(help="Cute foxgirls")
async def foxgirl(ctx):
    try:
        response = requests.get('http://api.nekos.fun:8080/api/foxgirl')
        response.raise_for_status()
        x = response.json()
        img = x["image"]
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    await ctx.send(img)

###

@bot.command(help="//DEBUG//")
async def embed(ctx, arg1, arg2, cr, cb, cg):
    embedVar = discord.Embed(title=arg1, description=arg2, color=discord.Color.from_rgb(int(cr), int(cb), int(cg)))
    await ctx.send(embed=embedVar)

############################################33
bot.run(os.getenv('TOKEN'))