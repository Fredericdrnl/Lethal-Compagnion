import discord
from discord.ext import commands

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ Bestiary ■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class BestiaryCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def bestiary(self, ctx):
        """Show a list of monsters."""
        bestiary=[{"name":"Monster 1","description":"Blabla"}, {"name":"Monster 2","description":"Blibli"}, {"name":"Monster 3","description":"Bloblo"}]
        embedBestiary = discord.Embed(title=f"Monsters' list",
                                    description="Monsters' summary",
                                    colour=discord.Colour.from_rgb(240, 128, 128),
	)
        for i in range (len(bestiary)):
            embedBestiary.add_field(name=bestiary[i].get("name"), value=bestiary[i].get("description"), inline=False)
        
        # embedPing.set_footer(text="By nous",
        #                     icon_url="https://i.goopics.net/encbhm.png")
        

        await ctx.send(embed=embedBestiary)

async def setup(bot):
    await bot.add_cog(BestiaryCommand(bot))