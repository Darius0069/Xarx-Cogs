from discord.ext import commands
import aiohttp
from bs4 import BeautifulSoup

class HS:
    """idk if I'll ever get this fucking shit to work"""
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 10, commands.BucketType.guild)
    async def hscard(self, ctx):
        """Should someday make it to search for a fucking card"""
        url = "https://steamdb.info/app/570/graphs/" #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            online = soupObject.find(class_='home-stats').find('li').find('strong').get_text()
            await self.bot.say(online + ' players are playing this game at the moment')
        except:
            await self.bot.say("Couldn't load amount of players. No one is playing this game anymore or there's an error.")

def __unload(self):
self.bot.loop.create_task(self.session.close())
