import discord
from discord.ext import commands

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ Store ■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class StoreCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def store(self, ctx):
        """Show the store's objects' list."""
        store=[{"name":"Object 1","description":"Blabla"}, {"name":"Object 2","description":"Blibli"}, {"name":"Object 3","description":"Bloblo"}]
        embedStore = discord.Embed(title=f"Objects' list",
                                    description="Objects' summary",
                                    colour=discord.Colour.from_rgb(240, 128, 128),
	)
        for i in range (len(store)):
            embedStore.add_field(name=store[i].get("name"), value=store[i].get("description"), inline=False)
        
        # embedPing.set_footer(text="By nous",
        #                     icon_url="https://i.goopics.net/encbhm.png")
        

        await ctx.send(embed=embedStore)

async def setup(bot):
    await bot.add_cog(StoreCommand(bot))