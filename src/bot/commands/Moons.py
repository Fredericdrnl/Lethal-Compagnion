import discord
from discord.ext import commands
import requests

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ Moons ■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class MoonsCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def moons(self, ctx):
        """Show information of all Moons."""
        response = requests.get("http://172.25.0.2:5000/Moons/")
        # Vérifier si la requête a réussi (code de statut HTTP 200)
        if response.status_code == 200:
            data = response.json()
            embedMoons = discord.Embed(title="All moons list",
                            colour=discord.Colour.from_rgb(240, 128, 128),
                            )
            for i in range(0, len(data)):
                embedMoons.add_field(name=data[i][1], value="Difficulty : " + data[i][2], inline=False)
        else:
            # Si la requête a échoué, imprimer le code de statut HTTP
            embedMoons = discord.Embed(title="Le monstre donné n'existe pas")

        await ctx.send(embed=embedMoons)

async def setup(bot):
    await bot.add_cog(MoonsCommand(bot))