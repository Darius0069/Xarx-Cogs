import discord
from redbot.core import commands
from random import choice

rmorningboss = [
    ("Random 1"),
    ("Random 2"),
    ("Random 3"),
    ("Random 4"),
    ("Random 5"),
    ("Random 6"),
    ("Random 7"),
    ("Random 8"),
    
]

class Morningboss(commands.Cog):

    """Based on Airenkun's Insult Cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["gmboss", "goodmorningboss"])
    async def morningboss(self, ctx, user: discord.Member = None):
        """
            Good morning to the user
        """

        msg = " "
        if user != None:

            if user.id == self.bot.user.id:
                user = ctx.message.author
                msg = [
                    (
                        " Morning Mr how are you? Hope doing great. Today i is raedy to go "
                    ),
                    (
                        " Morning boss hope doing great "
                    ),
                ]
                await ctx.send(user.mention + choice(msg))

            else:
                await ctx.send(user.mention + msg + choice(rmorningboss))
        else:
            await ctx.send(ctx.message.author.mention + msg + choice(rmorningboss))