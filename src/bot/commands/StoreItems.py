import discord
from discord.ext import commands
import requests

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ StoreItems ■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class StoreItemsCommand(commands.Cog):
    """
    This class create the "!StoreItems" command.
    This command show all store items.
    """
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def storeItems(self, ctx):
        """Show information of all StoreItems"""
        response = requests.get("http://127.0.0.1:5000/StoreItems/")
        data = response.json()
        if data != None or data != []:
            embedStoreItems = discord.Embed(title="All Store items list",
                            colour=discord.Colour.from_rgb(240, 128, 128),
                            )
            for i in range(0, len(data)):
                embedStoreItems.add_field(name=data[i][2], value=data[i][3], inline=False)
        else:
            embedStoreItems = discord.Embed(title="Le monstre donné n'existe pas")

        await ctx.send(embed=embedStoreItems)

async def setup(bot):
    await bot.add_cog(StoreItemsCommand(bot))