from .thesaurus import Thesaurus


def setup(bot):
    n = Thesaurus()
bot.add_cog(n)