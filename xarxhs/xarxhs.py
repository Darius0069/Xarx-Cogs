# Post animal pics by Eslyium#1949 & Yukirin#0048 is the original thingy
# I'm just using it for golden retrievers because of Lyutenitsa

# Discord
import discord
# Red
from redbot.core import commands
# Libs
import aiohttp

zam = "https://wow.zamimg.com/images/hearthstone/cards/enus/animated/"

BaseCog = getattr(commands, "Cog", object)


class Xarxhs(BaseCog):
    """Someday it might be just like a real cog"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
        self.zam = zam

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def cardg(self, ctx, name_or_id):
        """Show pokemon info"""

        try:
            headers = {"content-type": "application/json", "X-RapidAPI-Host": "omgvamp-hearthstone-v1.p.rapidapi.com", "X-RapidAPI-Key": "wXIuOpjmlRmsheQch0AYHKBPlGb0p1Z2Zf5jsnyZ5RwvU48gKY"}

            # Queries pokeapi for Name, ID and evolution_chain
            async with aiohttp.ClientSession() as session:
                async with session.get("https://omgvamp-hearthstone-v1.p.rapidapi.com/cards/" + name_or_id.lower(), headers=headers) as r1:
                    response1 = await r1.json()
                    await ctx.send(response1['img'])

        except:
            await ctx.send("No card found")
            return

#
#            # Conversion for embed
#            cardcost = str(response1["cost"]) + " mana"
#            cardattack = str(response1["attack"]) + " attack"
#            cardhealth = str(response1["health"]) + " health"
#            cardimg = str(response1["img"])
#            cardtxt = str(response1["text"])
#
#            # Build Embed
#            embed = discord.Embed()
#            embed.title = response1["name"].capitalize()
#            embed.description = cardtxt
#            embed.set_thumbnail(url=cardimg)
#            embed.add_field(name="Manacost", value=cost)
#            embed.add_field(name="Attack", value=attack)
#            embed.add_field(name="Health", value=health)
#            embed.set_footer(text="Powered by RapidAPI")
#            await ctx.send(embed=embed)

#        # Handles response1
#        if response1.get("detail") == "Not found.":
#            await ctx.send("No card found")
#        else:
#            cardname = response1["name"]
#
#            # Queries pokeapi for Height, Weight, Sprite
#            async with aiohttp.ClientSession() as session:
#                async with session.get("https://omgvamp-hearthstone-v1.p.rapidapi.com/cards/" + name_or_id.lower(), headers=headers) as r2:
#                    response2 = await r2.json()
#
#            # Queries pokeapi for Evolutions
#            async with aiohttp.ClientSession() as session:
#                async with session.get(str(text), headers=headers) as r3:
#                    response3 = await r3.json()
#
#            # Conversion for embed
#            cost = str(response2["cost"]) + "mana"
#            attack = str(response2["attack"]) + "attack"
#            health = str(response2["health"]) + "health"
#
#            # Build Embed
#            embed = discord.Embed()
#            embed.title = response1["name"].capitalize()
#            embed.description = description
#            embed.set_thumbnail(url=response2["img"])
#            embed.add_field(name="Cost", value=cost)
#            embed.add_field(name="Attack", value=attack)
#            embed.add_field(name="Health", value=health)
#            embed.set_footer(text="Powered by RapidAPI")
#            await ctx.send(embed=embed)
