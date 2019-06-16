import discord

from redbot.core import checks, commands

from typing import Union

from .core import Core

from random import choice

class Stuff:
    async def emoji(self):
        """Randomize footer emojis."""
        EMOJIS = [
            "\N{AUBERGINE}",
            "\N{SMIRKING FACE}",
            "\N{PEACH}",
            "\N{SPLASHING SWEAT SYMBOL}",
            "\N{BANANA}",
            "\N{KISS MARK}",
        ]
        emoji = choice(EMOJIS)
        return emoji
REDDIT_BASEURL = "https://api.reddit.com/r/"
REDDIT_ENDPOINT = "/random"
IMGUR_LINKS = "http://imgur.com", "https://m.imgur.com", "https://imgur.com"
GOOD_EXTENSIONS = ".png", ".jpg", ".jpeg", ".gif"
# Subreddits
FOODPORN = ["FoodPorn", "CulinaryPlating", "Pizza", "sexypizza", "steak"]
SHITTYFOODPORN = ["shittyfoodporn", "shittyfoodporn"]
EARTHPORN = ["EarthPorn", "EarthPorn"]
DESIGNPORN = ["DesignPorn", "DesignPorn"]
HELLSCAPEPORN = ["HellscapePorn", "HellscapePorn"]
APOCALYPSEPORN = ["ApocalypsePorn", "ApocalypsePorn"]
ARTPORN = ["ArtPorn", "ArtPorn"]

class Xreddit(Core, commands.Cog):
    """
        Send random foodporn/earthporn etc images from random subreddits.
    """
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(name="foodporn", aliases=["Foodporn", "FoodPorn", "FOODPORN"])
    async def foodporn(self, ctx):
        """Show some foodporn images from random subreddits."""

        await self._send_msg(ctx, "Foodporn", sub=FOODPORN)
