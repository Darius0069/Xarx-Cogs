import discord
from redbot.core import commands, Config, checks
import aiohttp
from redbot.core.utils.menus import menu, commands, DEFAULT_CONTROLS

BaseCog = getattr(commands, "Cog", object)


class Ritopls(BaseCog):
    """Shows shit info"""

    def __init__(self):
        self.config = Config.get_conf(self, identifier=244134642)
        default_global = {"apikey": ""}
        self.config.register_global(**default_global)
