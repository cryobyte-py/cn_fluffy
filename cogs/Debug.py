import discord
import requests
from requests import HTTPError
from discord.ext import commands
import sqlite3 as sl
class debug(commands.Cog, name='Debug'):
    def __init__(self, bot):
        self.bot = bot
    def setup(self, bot):
        bot.add_cog(debug(bot))
    @commands.command(help="//DEBUG//")
    async def join(self, context):
            if (context.author.voice):
                channel = context.author.voice.channel
                voice = await channel.connect()
                player = voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="testaud.mp3"))
            else:
                context.send("You must be in a voice channel")
    # Leave command, leaves the voice channel
    @commands.command(help="//DEBUG//")
    async def leave(self, context):
            await context.voice_client.disconnect()
    ###text format test###
    @commands.command(help="//DEBUG//")
    async def format(self, ctx,user: discord.User):
        await ctx.send("`{0} test ".format(ctx.author)+user.name+ "`")
    @commands.command(help="//DEBUG//")
    async def embed(self, ctx, arg1, arg2, cr, cb, cg):
        embedVar = discord.Embed(title=arg1, description=arg2, color=discord.Color.from_rgb(int(cr), int(cb), int(cg)))
        await ctx.send(embed=embedVar)
