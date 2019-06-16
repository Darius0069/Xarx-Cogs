from random import choice

# Stuff for the cog
class Stuff:
    async def emoji(self):
        """Randomize footer emojis."""
        EMOJIS = [
            "\N{AUBERGINE}",
            "\N{SMIRKING FACE}",
            "\N{PEACH}",
            "\N{SPLASHING SWEAT SYMBOL}",
            "\N{BANANA}",
            "\N{KISS MARK}",
        ]
        emoji = choice(EMOJIS)
        return emoji
    REDDIT_BASEURL = "https://api.reddit.com/r/"
    REDDIT_ENDPOINT = "/random"
    IMGUR_LINKS = "http://imgur.com", "https://m.imgur.com", "https://imgur.com"
    GOOD_EXTENSIONS = ".png", ".jpg", ".jpeg", ".gif"

    # Subreddits
    FOODPORN = ["FoodPorn", "CulinaryPlating", "Pizza", "sexypizza", "steak"]
    SHITTYFOODPORN = ["shittyfoodporn", "shittyfoodporn"]
    EARTHPORN = ["EarthPorn", "EarthPorn"]
    DESIGNPORN = ["DesignPorn", "DesignPorn"]
    HELLSCAPEPORN = ["HellscapePorn", "HellscapePorn"]
    APOCALYPSEPORN = ["ApocalypsePorn", "ApocalypsePorn"]
    ARTPORN = ["ArtPorn", "ArtPorn"]