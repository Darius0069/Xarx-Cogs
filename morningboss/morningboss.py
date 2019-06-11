import discord
from redbot.core import commands
from random import choice

rmorningboss = [
    (" Morning boss hope soing great I want to know I can get load of cookie "),
    (" Morning boss hope soing great I want to know i can get load of cokie "),
]

class Morningboss(commands.Cog):

    """Based on Airenkun's Insult Cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["gmboss", "goodmorningboss"])
    async def morningboss(self, ctx, user: discord.Member = None):
        """
            Morningboss-es the targetted user, or the invoker of the command if no user is selected
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