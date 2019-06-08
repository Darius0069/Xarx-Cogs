# Post animal pics by Eslyium#1949 & Yukirin#0048 is the original thingy
# I'm just using it for golden retrievers because of Lyutenitsa

# Discord
import discord
from discord import Webhook, AsyncWebhookAdapter
# Red
from redbot.core import commands
# Libs
import requests
import aiohttp

BaseCog = getattr(commands, "Cog", object)

class Whs(BaseCog):
    """Someday it might be just like a real cog"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    @commands.command()
    @commands.bot_has_permissions(manage_webhooks=True)
    async def hshook(self, ctx, lfcard):
        """Keep calm sigh"""
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('https://hearthstoneapi.com/webhook/slack', adapter=AsyncWebhookAdapter(session))
            await Webhook.send("I'm working!", username=lfcard)
