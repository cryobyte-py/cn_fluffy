from unicodedata import name
import discord
from discord.ext import commands

class Moderation(commands.cog, name="Moderation"):
    def __init__(self,bot):
        self.bot = bot
    ### TODO: REFINE MUTE
    #@commands.command(help="//DEBUG//")
    #async def roletest(self, ctx, target: discord.Member):
    #    if ctx.message.author.guild_permissions.administrator:
    #        mut = get(ctx.guild.roles, name = "Muted")
    #        await target.add_roles(mut)
    #@commands.command(help="//DEBUG//")
    #async def rolereturn(self, ctx):
    #    mut = get(ctx.guild.roles, name = "Muted")
    #    print(mut)
    #    if mut is None:
    #        print("Role not defined.")
    #        perms = discord.Permissions(send_messages=False, read_messages=True)
    #        await ctx.guild.create_role(name="Muted",perms=perms)
    #    await ctx.send(f"Mute ID:{mut}")
    @commands.command(help="Kicks the user")
    async def kick(self, ctx, target: discord.Member, reason=None):
        await target.kick(reason=reason)
        await ctx.send(f"{target} had been kicked. Reason: {reason}")
    @commands.command(help="Bans the user")
    async def ban(self, ctx, target: discord.Member, reason=None):
        await target.ban(reason=reason)
        await ctx.send(f"{target} had been banned. Reason: {reason}")