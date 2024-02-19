import discord
from discord.ext import commands
import requests

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ Monsters ■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class MonstersCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def monsters(self, ctx):
        """Show information of a monster."""
        response = requests.get("http://127.0.0.1:5000/Monsters/")
        # Vérifier si la requête a réussi (code de statut HTTP 200)
        if response.status_code == 200:
            data = response.json()
            embedMonsters = discord.Embed(title="All monster list",
                            colour=discord.Colour.from_rgb(240, 128, 128),
                            )
            print(data)
            for i in range(0, len(data) - 1):
                embedMonsters.add_field(name=data[i][1], value=data[i][2], inline=False)
        else:
            # Si la requête a échoué, imprimer le code de statut HTTP
            embedMonsters = discord.Embed(title="Le monstre donné n'existe pas")

        await ctx.send(embed=embedMonsters)

        

async def setup(bot):
    await bot.add_cog(MonstersCommand(bot))