# Post animal pics by Eslyium#1949 & Yukirin#0048 is the original thingy
# I'm just using it for golden retrievers because of Lyutenitsa

# Discord
import discord

# Red
from redbot.core import commands

# Libs
import aiohttp

grapi = "https://dog.ceo/api/breed/retriever/golden/images/random"

BaseCog = getattr(commands, "Cog", object)


class Gretriever(BaseCog):
    """Golden retriever commands."""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
        self.grapi = grapi

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def gretriever(self, ctx):
        """Shows a Golden Retriever"""
            async with self.session.get(self.grapi) as r:
                result = await r.json()
            await ctx.send(result['file'])


    def __unload(self):
        self.bot.loop.create_task(self.session.close())
    __del__ = __unload
