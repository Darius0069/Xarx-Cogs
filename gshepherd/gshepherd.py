# Post animal pics by Eslyium#1949 & Yukirin#0048 is the original thingy
# I'm just using it for golden retrievers because of Lyutenitsa

# Discord
import discord

# Red
from redbot.core import commands

# Libs
import aiohttp

goldenapi = "https://dog.ceo/api/breed/germanshepherd/images/random"

BaseCog = getattr(commands, "Cog", object)


class Gshepherd(BaseCog):
    """German shepherd commands, now does not have huskies!"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
        self.doggoapi = doggoapi

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.guild)
    async def gshepherd(self, ctx):
        """Shows a random german shepherd photo"""
        try:
            async with self.session.get(self.doggoapi) as r:
                result = await r.json()
            await ctx.send(result['message'])
        except:
            await ctx.send("API Error")

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.guild)
    async def gshepherds(self, ctx, amount : int = 5):
        """Throws a German shepherds bomb!
        Defaults to 5, max is 10 (thanks Eslyium#1949 & Yukirin#0048)"""
        results = []
        if amount > 10 or amount < 1:
            amount = 5
        try:
            for x in range(0,amount):
                async with self.session.get(self.doggoapi) as r:
                    api_result = await r.json()
                    results.append(api_result['message'])
            await ctx.send("\n".join(results))
        except:
            await ctx.send("API Error")

    def __unload(self):
        self.bot.loop.create_task(self.session.close())
