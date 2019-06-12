from .foodporn import Foodporn


def setup(bot):
    bot.add_cog(Foodporn(bot))
