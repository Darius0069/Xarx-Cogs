import discord
from redbot.core import commands, Config, checks
import aiohttp
from redbot.core.utils.menus import menu, commands, DEFAULT_CONTROLS

BaseCog = getattr(commands, "Cog", object)

class Thesaurus(BaseCog):
    """Shows synonyms and stuffs"""

    def __init__(self):
        self.config = Config.get_conf(self, identifier=900696642)
        default_global = {"apikey": ""}
self.config.register_global(**default_global)

@commands.command()
@checks.is_owner()
async def thesauruskey(self, ctx, *, key):
    """Set a key to use The Saurus API"""
    # Load
    config_boards = await self.config.apikey()
    # Set
    await self.config.apikey.set(key)
    await ctx.send("The apikey has been added.")