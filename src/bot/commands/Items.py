import discord
from discord.ext import commands

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■ Items ■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class ItemsCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def items(self, ctx):
        """Show the items's objects' list."""
        items=[{"name":"Item 1","description":"Blabla"}, {"name":"Item 2","description":"Blibli"}, {"name":"Item 3","description":"Bloblo"}]
        embedItems = discord.Embed(title=f"Items' list",
                                    description="Items' summary",
                                    colour=discord.Colour.from_rgb(240, 128, 128),
	)
        for i in range (len(items)):
            embedItems.add_field(name=items[i].get("name"), value=items[i].get("description"), inline=False)
        
        # embedPing.set_footer(text="By nous",
        #                     icon_url="https://i.goopics.net/encbhm.png")
        

        await ctx.send(embed=embedItems)

async def setup(bot):
    await bot.add_cog(ItemsCommand(bot))