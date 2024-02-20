import discord
from discord.ext import commands
import requests

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ Moon ■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class MoonCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def moon(self, ctx, MoonName : str):
        """Show information of a Moon."""
        response = requests.get(f"http://127.0.0.1:5000/Moons/{MoonName}")
        # Vérifier si la requête a réussi (code de statut HTTP 200)
        data = response.json()
        if response.status_code == 200:
            embedMoon = discord.Embed(title=str(data[0][1]),
                            description="",
                            colour=discord.Colour.from_rgb(240, 128, 128),
                            )
            embedMoon.add_field(name="Difficulty", value=str(data[0][2]), inline=False)
            embedMoon.add_field(name="Cost Moon", value=str(data[0][3]), inline=False)
            embedMoon.add_field(name="Weather", value=str(data[0][4]), inline=False)
            embedMoon.add_field(name="Default Layout", value=str(data[0][5]), inline=False)
            embedMoon.add_field(name="Min Scrap", value=str(data[0][6]), inline=False)
            embedMoon.add_field(name="Max Scrap", value=str(data[0][7]), inline=False)
        else:
            # Si la requête a échoué, imprimer le code de statut HTTP
            embedMoon = discord.Embed(title="Le monstre donné n'existe pas")
            
        embedMoon.set_thumbnail(url=data[0][8])
    
        await ctx.send(embed=embedMoon)

async def setup(bot):
    await bot.add_cog(MoonCommand(bot))