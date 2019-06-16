import discord

from redbot.core import checks, commands

from typing import Union

from .constants import Stuff as sub
from .core import Core

class Xreddit(Core, commands.Cog):
    """
        Send random foodporn/earthporn etc images from random subreddits.
    """
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(name="foodporn", aliases=["Foodporn", "FoodPorn", "FOODPORN"])
    async def foodporn(self, ctx):
        """Show some foodporn images from random subreddits."""

        await self._send_msg(ctx, "Foodporn", sub=sub.FOODPORN)
