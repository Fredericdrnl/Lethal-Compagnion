import discord
from discord.ext import commands
import requests

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ StoreItem ■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class StoreItemCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def storeItem(self, ctx, StoreItemName : str):
        """Show information of a StoreItem."""
        response = requests.get(f"http://127.0.0.1:5000/StoreItems/{StoreItemName}")
        # Vérifier si la requête a réussi (code de statut HTTP 200)
        data = response.json()
        if response.status_code == 200:
            embedStoreItem = discord.Embed(title=str(data[0][1]),
                                description="",
                                colour=discord.Colour.from_rgb(240, 128, 128),
                            )
            embedStoreItem.add_field(name="Entry Store", value=str(data[0][3]), inline=False)
            embedStoreItem.add_field(name="Cost Store", value=str(data[0][4]), inline=False)
            embedStoreItem.add_field(name="Weight", value=str(data[0][5]), inline=False)
            if data[0][6] == "false":
                embedStoreItem.add_field(name="Conductive", value="Not conductive store item", inline=False)
            else:
                embedStoreItem.add_field(name="Conductive", value="conductive store item", inline=False)
            embedStoreItem.add_field(name="Battery Store", value=str(data[0][7]), inline=False)
        else:
            # Si la requête a échoué, imprimer le code de statut HTTP
            embedStoreItem = discord.Embed(title="Le monstre donné n'existe pas")
            
        embedStoreItem.set_thumbnail(url=data[0][8])
    
        await ctx.send(embed=embedStoreItem)

async def setup(bot):
    await bot.add_cog(StoreItemCommand(bot))