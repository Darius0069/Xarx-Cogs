from redbot.core import commands
from discord.ext import commands
import urllib.request
from bs4 import BeautifulSoup

class HS(commands.Cog):
    """WIP HS Thing"""

    @commands.command()
    async def hsping(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")
