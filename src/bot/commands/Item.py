import discord
from discord.ext import commands
import requests

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ Item ■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class ItemCommand(commands.Cog):
    """
    Class who create the "!Item <ItemName>" command.
    This one show all information about one item.
    """
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def item(self, ctx, ItemName : str):
        """
        Show information of a Item.
        
        Args:
            ItemName (str) : Item which show her information.
        """
        response = requests.get(f"http://127.0.0.1:5000/Items/{ItemName}")
        data = response.json()
        if data != None or data != []:
            embedItem = discord.Embed(title=str(data[0][2]),
                            description="",
                            colour=discord.Colour.from_rgb(240, 128, 128),
                            )
            embedItem.add_field(name="Description", value=str(data[0][3]), inline=False)
            embedItem.add_field(name="Cost", value="Min : " + str(data[0][4]) + " Max : " + str(data[0][5]), inline=False)
            embedItem.add_field(name="weight", value=str(data[0][5]), inline=False)
            if data[0][7] == "false":
                embedItem.add_field(name="Conductive", value="Not conductive scrap", inline=False)
            else:
                embedItem.add_field(name="Conductive", value="conductive scrap", inline=False)

            if data[0][8] == "false":
                embedItem.add_field(name="Hand", value="One handed", inline=False)
            else:
                embedItem.add_field(name="Hand", value="two handed", inline=False)
            embedItem.set_thumbnail(url=data[0][9])
        else:
            embedItem = discord.Embed(title="Le monstre donné n'existe pas")
            

    
        await ctx.send(embed=embedItem)

async def setup(bot):
    await bot.add_cog(ItemCommand(bot))