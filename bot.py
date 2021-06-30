import discord
import os
import discord.ext.commands
from dotenv.main import load_dotenv 
import json

################## INITIATE ################################

load_dotenv()
bot = discord.ext.commands.Bot(command_prefix="..!")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name="Test mode initiated"))

f = open("db.json","r")
foo = {}
foo = json.load(f)
f.close
print(foo)

############################################################

## COMMAND:
# @bot.command()
# async def <COMMAND NAME>(ctx, <insert args>):

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
@bot.command()
async def con(ctx):
    print("success")
@bot.command()
async def hug(ctx, arg):
    await ctx.send("<@"+str(ctx.author.id)+">" + " hugs " + arg)
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
    await ctx.send(embed=embedHelp)
    
bot.run(os.getenv('TOKEN'))
