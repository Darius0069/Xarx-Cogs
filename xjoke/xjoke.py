# Discord
import discord

# Red
from redbot.core import commands

# Libs
import aiohttp
import time

programmingx = "https://sv443.net/jokeapi/category/Programming"
miscx = "https://sv443.net/jokeapi/category/Miscellaneous"
darkx = "https://sv443.net/jokeapi/category/Dark"
anyx = "https://sv443.net/jokeapi/category/Any"

BaseCog = getattr(commands, "Cog", object)


class Xjoke(BaseCog):
    """Posts a joke!"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
        self.programming = programmingx
        self.misc = miscx
        self.dark = darkx
        self.any = anyx
    

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.guild)
    async def goldendoggo(self, ctx, *, argx):
        """Let's try a joke"""
        try:
            async with self.session.get(self.argx) as r:
                result = await r.json()
            if result['type'] = twopart:
                await ctx.send(result['setup'])
                time.sleep(.5)
                await ctx.send(result['delivery'])
            else:
                await ctx.send(result['joke'])
        except:
            await ctx.send("API Error")

            
    def __unload(self):
        self.bot.loop.create_task(self.session.close())
