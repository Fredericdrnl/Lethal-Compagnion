import discord
from discord.ext import commands
import requests

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ Monsters ■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class MonstersCommand(commands.Cog):
    """
    This class create the "!monsters" command.
    This command show all monsters of Lethal Company.
    """
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def monsters(self, ctx):
        """Show all Monsters."""
        response = requests.get("http://127.0.0.1:5000/Monsters/")
        data = response.json()
        if data != None or data != []:
            embedMonsters = discord.Embed(title="All monster list",
                            colour=discord.Colour.from_rgb(240, 128, 128),
                            )
            for i in range(0, len(data) - 1):
                embedMonsters.add_field(name=data[i][2], value=data[i][3], inline=False)
        else:
            embedMonsters = discord.Embed(title="Le monstre donné n'existe pas")

        await ctx.send(embed=embedMonsters)

        

async def setup(bot):
    await bot.add_cog(MonstersCommand(bot))