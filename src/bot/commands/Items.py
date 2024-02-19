import discord
from discord.ext import commands
import requests

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ Items ■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class ItemsCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def items(self, ctx):
        """Show information of a monster."""
        response = requests.get("http://127.0.0.1:5000/Items/")
        # Vérifier si la requête a réussi (code de statut HTTP 200)
        if response.status_code == 200:
            data = response.json()
            embedItems = discord.Embed(title="All items list",
                            colour=discord.Colour.from_rgb(240, 128, 128),
                            )
            
            embedItems2 = discord.Embed(title="",
                            colour=discord.Colour.from_rgb(240, 128, 128),
                            )
            
            embedItems3 = discord.Embed(title="",
                            colour=discord.Colour.from_rgb(240, 128, 128),
                            )
            
            for i in range(0, 20):
                embedItems.add_field(name=data[i][1], value=data[i][2], inline=False)

            for i in range(21, 40):
                embedItems2.add_field(name=data[i][1], value=data[i][2], inline=False)

            for i in range(41, len(data)):
                embedItems3.add_field(name=data[i][1], value=data[i][2], inline=False)

            await ctx.send(embed=embedItems)
            await ctx.send(embed=embedItems2)
            await ctx.send(embed=embedItems3)

        else:
            # Si la requête a échoué, imprimer le code de statut HTTP
            embedItems = discord.Embed(title="Le monstre donné n'existe pas")

            await ctx.send(embed=embedItems)

        

async def setup(bot):
    await bot.add_cog(ItemsCommand(bot))