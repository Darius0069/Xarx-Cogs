from .todostuff import Todostuff


def setup(bot):
    bot.add_cog(Todostuff(bot))
