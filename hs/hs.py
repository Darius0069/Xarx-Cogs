import discord
import aiohttp
from redbot.core import commands
import urllib.request
from bs4 import BeautifulSoup

class HS(commands.Cog):
    """WIP HS Thing"""

    @commands.command()
    async def hsping(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")

    @commands.command()
    async def card(self, *text):
        """Retrieves card art from a hearthpwn search"""
        if len(text) > 0:
            try:
                card = '+'.join([str(x) for x in text]) # convert the text list into a string joined by + characters for use in a web address
                url = "http://www.hearthpwn.com/cards?filter-name="+card #build the web adress
                soupObject = BeautifulSoup(urllib.request.urlopen(url), "html.parser") # get the web page and create a BeautifulSoup4 object
                img = soupObject.find("img")["src"] #find the first image tag and return the source attribute
                await self.bot.say(img)
            except:
                await self.bot.say("`Could not find that card, check your spelling or try another card.`")
        else:
            await self.bot.say("```card [name]\n\nSearches http://www.hearthpwn.com/\nReturns first available card that matches the search text.\nUse \"cardg\" to get gold cards.```")
