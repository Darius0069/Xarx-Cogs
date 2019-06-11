import discord
from redbot.core import commands
from random import choice

rmorningboss = [
    _("Random 1"),
    _("Random 2"),
    _("Random 3"),
    _("Random 4"),
    _("Random 5"),
    _("Random 6"),
    _("Random 7"),
    _("Random 8"),
    
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
                    _(
                        " Morning Mr how are you? Hope doing great. Today i is raedy to go"
                    ),
                    _(
                        " Morning boss hope doing great "
                    ),
                ]
                await ctx.send(user.mention + choice(msg))

            else:
                await ctx.send(user.mention + msg + choice(rmorningboss))
        else:
            await ctx.send(ctx.message.author.mention + msg + choice(rmorningboss))