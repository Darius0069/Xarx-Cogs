import asyncio
import discord
import random
from redbot.core import Config
from redbot.core import commands

class Todostuff(BaseCog):
    """I ain't got an idea if this will ever work"""

    def __init__(self):
        self.config = Config.get_conf(self, identifier=900697142, force_registration=True)
        default_user = {"Stuffs": ""}
        self.config.register_global(**default_global)
        self.config.register_global(
            stuffs=("Nothing")
        )

@commands.command()
async def todo(self, ctx, addtodo):
    user_group = self.config.user(ctx.user)
    async with user_group.todo() as todo1:
        todo.append(addtodo)
    await ctx.send("The new [todo] value has been added!")