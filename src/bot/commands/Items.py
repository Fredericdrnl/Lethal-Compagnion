import discord
from discord.ext import commands
import requests

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ Items ■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class ItemsCommand(commands.Cog):
    """
    This class create the Items command.
    he can show all items which are in game.
    """
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def items(self, ctx):
        """Show all Items in Lethal Company."""
        response = requests.get("http://127.0.0.1:5000/Items/")
        data = response.json()
        if data != None or data != []:
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
                embedItems.add_field(name=data[i][2], value=data[i][3], inline=False)

            for i in range(21, 40):
                embedItems2.add_field(name=data[i][2], value=data[i][3], inline=False)

            for i in range(41, len(data)):
                embedItems3.add_field(name=data[i][2], value=data[i][3], inline=False)

            await ctx.send(embed=embedItems)
            await ctx.send(embed=embedItems2)
            await ctx.send(embed=embedItems3)

        else:
            embedItems = discord.Embed(title="Le monstre donné n'existe pas")
            await ctx.send(embed=embedItems)

        
async def setup(bot):
    await bot.add_cog(ItemsCommand(bot))