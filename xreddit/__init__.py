from .xreddit import Xreddit


def setup(bot):
    n = Xreddit(bot)
bot.add_cog(n)