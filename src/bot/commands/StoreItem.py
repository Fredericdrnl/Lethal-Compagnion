import discord
from discord.ext import commands
import requests

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ StoreItem ■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class StoreItemCommand(commands.Cog):
    """
    This class create "!StoreItem <StoreItemName>" command.
    That command show all information about one item.
    """
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def storeItem(self, ctx, StoreItemName : str):
        """
        Show information of a StoreItem.
        
        Args:
            StoreItemName (str) : Store item which show her information.
        """
        response = requests.get(f"http://127.0.0.1:5000/StoreItems/{StoreItemName}")
        data = response.json()
        if data != [] and data != None:
            embedStoreItem = discord.Embed(title=str(data[0][1]),
                                description="",
                                colour=discord.Colour.from_rgb(240, 128, 128),
                            )
            embedStoreItem.add_field(name="Entry Store", value=str(data[0][3]), inline=False)
            embedStoreItem.add_field(name="Cost Store", value=str(data[0][4]), inline=False)
            embedStoreItem.add_field(name="Weight", value=str(data[0][5]), inline=False)
            if data[0][6] == "false":
                embedStoreItem.add_field(name="Conductive", value="Not conductive store item", inline=False)
            else:
                embedStoreItem.add_field(name="Conductive", value="conductive store item", inline=False)
            embedStoreItem.add_field(name="Battery Store", value=str(data[0][7]), inline=False)
            embedStoreItem.set_thumbnail(url=data[0][8])
        else:
            embedStoreItem = discord.Embed(title="Le monstre donné n'existe pas")
            
        await ctx.send(embed=embedStoreItem)

async def setup(bot):
    await bot.add_cog(StoreItemCommand(bot))