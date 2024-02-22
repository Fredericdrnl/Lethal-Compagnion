import discord
from discord.ext import commands
import requests

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ Moons ■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class MoonsCommand(commands.Cog):
    """
    This class make the "!moons" command.
    This command show all Moons.
    """
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def moons(self, ctx):
        """Show information of all Moons."""
        response = requests.get("http://127.0.0.1:5000/Moons/")
        data = response.json()
        if data != None or data != []:
            embedMoons = discord.Embed(title="All moons list",
                            colour=discord.Colour.from_rgb(240, 128, 128),
                            )
            for i in range(0, len(data)):
                embedMoons.add_field(name=data[i][1], value="Difficulty : " + data[i][2], inline=False)
        else:
            embedMoons = discord.Embed(title="Le monstre donné n'existe pas")

        await ctx.send(embed=embedMoons)

async def setup(bot):
    await bot.add_cog(MoonsCommand(bot))