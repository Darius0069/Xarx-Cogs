import discord
from redbot.core import commands
import urllib.request
import unirest
import aiohttp

BaseCog = getattr(commands, "Cog", object)

class HS(BaseCog):
    """WIP HS Thing"""

    def __init__(self, bot):
        self.bot = bot

response = unirest.get("https://irythia-hs.p.rapidapi.com/card?name=Ysera",
  headers={
    "X-RapidAPI-Host": "irythia-hs.p.rapidapi.com",
    "X-RapidAPI-Key": "wXIuOpjmlRmsheQch0AYHKBPlGb0p1Z2Zf5jsnyZ5RwvU48gKY"
  }
)

@commands.command()
async def hsping(self, ctx):
    """This does stuff!"""
    # Your code will go here
    await ctx.send(response)
