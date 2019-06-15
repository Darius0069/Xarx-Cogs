from .gshepherd import Gshepherd


def setup(bot):
    bot.add_cog(Gshepherd(bot))
