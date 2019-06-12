# Post animal pics by Eslyium#1949 & Yukirin#0048 is the original thingy
# I'm just using it for golden retrievers because of Lyutenitsa

# Discord
import discord

# Red
from redbot.core import commands

# Libs
import aiohttp
import time
import praw
import random

BaseCog = getattr(commands, "Cog", object)

LIMIT_POST = 10

class Foodporn(BaseCog):
    """Gets a random thing from /r/foodporn"""

    def __init__(self, bot):
        self.bot = bot
        self.subreddit = reddit.subreddit("foodporn")
        self.newsubmissions = subreddit.new(limit = LIMIT_POST)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.guild)
    async def foodporn(self, ctx):
        """Gets a random thing from /r/foodporn"""
        try:
            async with self.newsubmissions:
                    current_time = int(time.time())
                    posts = []

                    for submission in newsubmissions
                        subage = ((current_time - submission.created_utc) /60 /60 /24)
                        if subage < 1:
                            posts.append(submission)

                    random_number = random.randit(0,LIMIT_POST -1)
                    random_post = posts[random_number]
            
            await ctx.send(random_post)
        except:
            await ctx.send("Some shit went very wrong")