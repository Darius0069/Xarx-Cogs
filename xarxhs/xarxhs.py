# Post animal pics by Eslyium#1949 & Yukirin#0048 is the original thingy
# I'm just using it for golden retrievers because of Lyutenitsa

# Discord
import discord
# Red
import redbot.core
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
            headers = {"content-type": "application/json"}

            # Queries pokeapi for Name, ID and evolution_chain
            async with aiohttp.ClientSession() as session:
                async with session.get("https://pokeapi.co/api/v2/pokemon-species/" + name_or_id.lower(), headers=headers) as r1:
                    response1 = await r1.json()

        except:
            await ctx.send("No pokemon found")
            return


        # Handles response1
        if response1.get("detail") == "Not found.":
            await ctx.send("No pokemon found")
        else:
            evolution_url = response1["evolution_chain"]["url"]

            # Queries pokeapi for Height, Weight, Sprite
            async with aiohttp.ClientSession() as session:
                async with session.get("https://pokeapi.co/api/v2/pokemon/" + name_or_id.lower(), headers=headers) as r2:
                    response2 = await r2.json()

            # Queries pokeapi for Evolutions
            async with aiohttp.ClientSession() as session:
                async with session.get(str(evolution_url), headers=headers) as r3:
                    response3 = await r3.json()

            # Selects english description for embed
            description = ""
            for i in range(0, len(response1["flavor_text_entries"])):
                if response1["flavor_text_entries"][i]["language"]["name"] == "en":
                    description = response1["flavor_text_entries"][i]["flavor_text"]
                    break

            # Conversion for embed
            height = str(response2["height"] / 10.0) + "m"
            weight = str(response2["weight"] / 10.0) + "kg"

            # Deals with evolution_chain for presentation in embed
            evolution = response3["chain"]["evolves_to"]
            evolutions = [response3["chain"]["species"]["name"].capitalize()]
            while len(evolution) > 0:
                evolutions.append(evolution[0]["species"]["name"].capitalize())
                evolution = evolution[0]["evolves_to"]
            if len(evolutions) == 1:
                evolution_string = "No evolutions"
            else:
                evolution_string = " -> ".join(evolutions)

            # Build Embed
            embed = discord.Embed()
            embed.title = response1["name"].capitalize()
            embed.description = description
            embed.set_thumbnail(url=response2["sprites"]["front_default"])
            embed.add_field(name="Evolutions", value=evolution_string, inline=False)
            embed.add_field(name="Height", value=height)
            embed.add_field(name="Weight", value=weight)
            embed.set_footer(text="Powered by Pokeapi")
            await ctx.send(embed=embed)
