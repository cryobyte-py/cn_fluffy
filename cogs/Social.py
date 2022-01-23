import discord
import requests
from requests import HTTPError
from discord.ext import commands

class Social(commands.Cog, name='Social'):
    def __init__(self, bot):
        self.bot = bot
    def setup (self,bot):
        bot.add_cog(Social(bot))

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f'Hey {ctx.author.name}')
    @commands.command(help="Hugs a user")
    async def hug(self, ctx, user: discord.User):
        try:
            response = requests.get('http://api.nekos.fun:8080/api/hug')
            response.raise_for_status()
            x = response.json()
            img = x["image"]
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        socialEmbed = discord.Embed(title="{0} hugs ".format(ctx.author.name)+user.name,color = discord.Color.from_rgb(100,240,20))
        socialEmbed.set_image(url=img)
        await ctx.send(embed=socialEmbed)
    @commands.command(help="Kisses a user")
    async def kiss(self, ctx, user: discord.User):
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
    @commands.command(help="Pats a user")
    async def pat(self, ctx, user: discord.User):
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
    @commands.command(help="Cuddles a user")
    async def cuddle(self, ctx, user: discord.User):
        try:
            response = requests.get('http://api.nekos.fun:8080/api/cuddle')
            response.raise_for_status()
            x = response.json()
            img = x["image"]
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        socialEmbed = discord.Embed(title="{0} cuddles ".format(ctx.author)+user.name+" >^<",color = discord.Color.from_rgb(100,240,20))
        socialEmbed.set_image(url=img)
        await ctx.send(embed=socialEmbed)
    @commands.command(help="Tickles a user")
    async def tickle(self, ctx, user: discord.User):
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
    @commands.command(help="Pokes a user")
    async def poke(self, ctx, user: discord.User):
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
    @commands.command(help="Boop a user")
    async def boop(self, ctx, user: discord.User):
        try:
            response = requests.get('http://api.nekos.fun:8080/api/poke')
            response.raise_for_status()
            x = response.json()
            img = x["image"]
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        socialEmbed = discord.Embed(title="{0} boops ".format(ctx.author)+user.name,color = discord.Color.from_rgb(100,240,20))
        socialEmbed.set_image(url=img)
        await ctx.send(embed=socialEmbed)
    @commands.command(help="Slaps a user")
    async def slap(self, ctx, user: discord.User):
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
    @commands.command(help="Feeds a user")
    async def feed(self, ctx, user: discord.User):
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
    @commands.command(help="Licks a user")
    async def lick(self, ctx, user: discord.User):
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
    @commands.command(help="Smug :3")
    async def smug(self, ctx):
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
    @commands.command(help="Cry ;w;")
    async def cry(self, ctx):
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
    @commands.command(help="hahahaha :D")
    async def laugh(self, ctx):
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
    @commands.command(help="Sends a cute fox")
    async def fox(self, ctx):
        r = requests.get("https://randomfox.ca/floof/")
        foo = r.text
        foo = foo.split('"')[3]
        foo = foo.split("/")[4]
        await ctx.send("https://randomfox.ca/images/" + foo)
    @commands.command(help="Cute foxgirls")
    async def foxgirl(self, ctx):
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