# Post animal pics by Eslyium#1949 & Yukirin#0048 is the original thingy
# I'm just using it for golden retrievers because of Lyutenitsa

# Discord
import discord
# Red
import redbot.core
# Libs
import aiohttp

zam = "https://wow.zamimg.com/images/hearthstone/cards/enus/animated/"

BaseCog = getattr(commands, "Cog", object)


class Xarxhs(BaseCog):
    """Someday it might be just like a real cog"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
        self.zam = zam

    @commands.command()
    async def gcard(self, ctx, *, cardname) # Grabs the card name.
        await ctx.send(cardname)

    def __unload(self):
        self.bot.loop.create_task(self.session.close())
