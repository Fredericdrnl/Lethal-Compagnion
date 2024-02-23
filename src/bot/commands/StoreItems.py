import discord
from discord.ext import commands
import requests

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ StoreItems ■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class StoreItemsCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def storeItems(self, ctx):
        """Show information of all StoreItems"""
        response = requests.get("http://172.25.0.2:5000/StoreItems/")
        # Vérifier si la requête a réussi (code de statut HTTP 200)
        if response.status_code == 200:
            data = response.json()
            embedStoreItems = discord.Embed(title="All Store items list",
                            colour=discord.Colour.from_rgb(240, 128, 128),
                            )
            for i in range(0, len(data)):
                embedStoreItems.add_field(name=data[i][1], value=data[i][2], inline=False)
        else:
            #Si la requête a échoué, imprimer le code de statut HTTP
            embedStoreItems = discord.Embed(title="Le monstre donné n'existe pas")

        await ctx.send(embed=embedStoreItems)

async def setup(bot):
    await bot.add_cog(StoreItemsCommand(bot))