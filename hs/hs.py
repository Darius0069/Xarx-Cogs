import discord
from redbot.core import commands
import urllib.request
import aiohttp
import requests

BaseCog = getattr(commands, "Cog", object)

class HS(BaseCog):
    """WIP HS Thing"""

    def __init__(self, bot):
        self.bot = bot

url = 'https://omgvamp-hearthstone-v1.p.rapidapi.com/cards/ysera'

param = {
    "X-RapidAPI-Host": "omgvamp-hearthstone-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "wXIuOpjmlRmsheQch0AYHKBPlGb0p1Z2Zf5jsnyZ5RwvU48gKY"
}

response = requests.get(url, headers=param)

@commands.command()
async def hsping(self, ctx):
    """This does stuff!"""
    # Your code will go here
    await ctx.send(response)
