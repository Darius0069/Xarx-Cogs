# Post animal pics by Eslyium#1949 & Yukirin#0048 is the original thingy
# I'm just using it for golden retrievers because of Lyutenitsa

# Discord
import discord

# Red
from redbot.core import commands

# Libs
import aiohttp

foodpornapi = "http://www.reddit.com/r/FoodPorn.json"

BaseCog = getattr(commands, "Cog", object)


class Foodporn(BaseCog):
    """Gets a random thing from /r/foodporn"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
        self.foodpornapi = foodpornapi

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.guild)
    async def foodporn(self, ctx):
        """Gets a random thing from /r/foodporn"""
        try:
            async with self.session.get(self.foodpornapi) as r:
                result = await r.json(body)

                urls = [ ]
                for child in result.data.children
                    if child.data.comain != "self.foodporn"
                        urls.push(child.data.url)

                if urls.count <= 0
                    await ctx.send("Couldn't find anything tastey :(")
                    return

            rnd = Math.floor(Math.random()*urls.length)
            picked_url = urls[rnd]

            persed_url = url.parse(picked_url)
            if parsed_url.host == "imgur.com"
                parsed_url.host = "i.imgur.com"
                parsed_url.pathname = parsed_url.pathname + ".jpg"

                picked_url = url.format(parsed_url)
            
            await ctx.send(picked_url)
        except:
            await ctx.send("API Error")

    def __unload(self):
        self.bot.loop.create_task(self.session.close())
