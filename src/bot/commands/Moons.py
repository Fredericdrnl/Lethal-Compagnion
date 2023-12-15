import discord
from discord.ext import commands

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■ Moons ■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class MoonsCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def moons(self, ctx):
        """Show the moons's objects' list."""
        moons=[{"name":"Moon 1","description":"Blabla"}, {"name":"Moon 2","description":"Blibli"}, {"name":"Moon 3","description":"Bloblo"}]
        embedMoons = discord.Embed(title=f"Moons' list",
                                    description="Moons' summary",
                                    colour=discord.Colour.from_rgb(240, 128, 128),
	)
        for i in range (len(moons)):
            embedMoons.add_field(name=moons[i].get("name"), value=moons[i].get("description"), inline=False)
        
        # embedPing.set_footer(text="By nous",
        #                     icon_url="https://i.goopics.net/encbhm.png")
        

        await ctx.send(embed=embedMoons)

async def setup(bot):
    await bot.add_cog(MoonsCommand(bot))