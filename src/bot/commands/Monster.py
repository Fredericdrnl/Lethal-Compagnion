import discord
from discord.ext import commands
import requests

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ Monster ■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class MonsterCommand(commands.Cog):
    """
    This class create the command "Monster <MonsterName>"
    Show all information about one monster.
    """
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def monster(self, ctx, MonsterName : str):
        """
        Show information of a Monster.
        
        Args:
            MonsterName (str) : Monster which show her information.
        """
        response = requests.get(f"http://127.0.0.1:5000/Monsters/{MonsterName}")
        data = response.json()
        if data != None or data != []:
            embedBestiary = discord.Embed(title=str(data[0][2]),
                            description="Monsters' summary",
                            colour=discord.Colour.from_rgb(240, 128, 128),
                            )
            embedBestiary.add_field(name="Description", value=str(data[0][3]), inline=False)
            embedBestiary.add_field(name="Particularity", value=str(data[0][4]), inline=False)
            embedBestiary.add_field(name="Strategy", value=str(data[0][5]), inline=False)
        else:
            embedBestiary = discord.Embed(title="Le monstre donné n'existe pas")
            
        embedBestiary.set_thumbnail(url=data[0][6])
        
        await ctx.send(embed=embedBestiary)

async def setup(bot):
    await bot.add_cog(MonsterCommand(bot))