import discord
from discord.ext import commands
import requests

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ Item ■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class ItemCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def item(self, ctx, ItemName : str):
        """Show information of a Item."""
        response = requests.get(f"http://127.0.0.1:5000/Items/{ItemName}")
        # Vérifier si la requête a réussi (code de statut HTTP 200)
        data = response.json()
        if response.status_code == 200:
            embedItem = discord.Embed(title=str(data[0][2]),
                            description="",
                            colour=discord.Colour.from_rgb(240, 128, 128),
                            )
            embedItem.add_field(name="Description", value=str(data[0][3]), inline=False)
            embedItem.add_field(name="Cost", value="Min : " + str(data[0][4]) + " Max : " + str(data[0][5]), inline=False)
            embedItem.add_field(name="weight", value=str(data[0][5]), inline=False)
            if data[0][7] == "false":
                embedItem.add_field(name="Conductive", value="Not conductive scrap", inline=False)
            else:
                embedItem.add_field(name="Conductive", value="conductive scrap", inline=False)

            if data[0][8] == "false":
                embedItem.add_field(name="Hand", value="One handed", inline=False)
            else:
                embedItem.add_field(name="Hand", value="two handed", inline=False)
        else:
            # Si la requête a échoué, imprimer le code de statut HTTP
            embedItem = discord.Embed(title="Le monstre donné n'existe pas")
            
        embedItem.set_thumbnail(url=data[0][9])
    
        await ctx.send(embed=embedItem)

async def setup(bot):
    await bot.add_cog(ItemCommand(bot))