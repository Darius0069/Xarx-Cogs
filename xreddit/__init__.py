from .xreddit import Xreddit


def setup(bot):
    bot.add_cog(Xreddit(bot))