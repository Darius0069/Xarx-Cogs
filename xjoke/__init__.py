from .xjoke import Xjoke


def setup(bot):
    bot.add_cog(Xjoke(bot))
