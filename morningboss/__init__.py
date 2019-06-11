from .whs import Whs


def setup(bot):
    bot.add_cog(Morningboss(bot))
