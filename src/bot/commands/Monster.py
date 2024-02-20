import discord
from discord.ext import commands
import requests

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ Monster ■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class BestiaryCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def monster(self, ctx, monsterName : str):
        """Show information of a Monster."""
        response = requests.get(f"http://127.0.0.1:5000/Monsters/{monsterName}")
        # Vérifier si la requête a réussi (code de statut HTTP 200)
        data = response.json()
        if response.status_code == 200:
            embedBestiary = discord.Embed(title=str(data[0][2]),
                            description="Monsters' summary",
                            colour=discord.Colour.from_rgb(240, 128, 128),
                            )
            embedBestiary.add_field(name="Description", value=str(data[0][3]), inline=False)
            embedBestiary.add_field(name="Particularity", value=str(data[0][4]), inline=False)
            embedBestiary.add_field(name="Strategy", value=str(data[0][5]), inline=False)
        else:
            # Si la requête a échoué, imprimer le code de statut HTTP
            embedBestiary = discord.Embed(title="Le monstre donné n'existe pas")
            
        embedBestiary.set_thumbnail(url=data[0][6])
        
        await ctx.send(embed=embedBestiary)

async def setup(bot):
    await bot.add_cog(BestiaryCommand(bot))