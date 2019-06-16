import discord

from redbot.core import checks, commands

from typing import Union

from .constants import Stuff as sub
from .core import Core

class Xreddit(Core, commands.Cog):
    """
        Send random foodporn/earthporn etc images from random subreddits.
    """

    authorx = ["Predä", "aikaterna", "Darius"]
    versionx = "Based on: 2.1.0"

    @commands.command()
    async def xredditversion(self, ctx):
        """Get the version of the installed Nsfw cog. Xreddit is based on it."""

        await self._version_msg(ctx, self.versionx, self.authorx)

    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(name="FOODPORN", aliases=["Foodporn", "FoodPorn"])
    async def foodporn(self, ctx):
        """Show some foodporn images from random subreddits."""

        await self._send_msg(ctx, _("Foodporn"), sub=sub.FOODPORN)
