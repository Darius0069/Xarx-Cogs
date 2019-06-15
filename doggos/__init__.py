from .gretriever import Gretriever


def setup(bot):
    bot.add_cog(Gretriever(bot))
