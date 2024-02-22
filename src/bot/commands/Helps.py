import discord
from discord.ext import commands

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ Help ■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class HelpsCommand(commands.Cog):
    """
    This class create the "!helps" command.
    This command show all is possible with the discord bot.
    """
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        self.commands = {
            "!monsters" : "Show all monsters name with description.",
            "!monster <MonsterName>" : "Show lot of information about the monster on the command.",
            "!moons" : "Show all moon name with difficulty.",
            "!moon <MoonName>" : "Show lot of information about Moon ont the command.",
            "!items" : "Show all item name with description.",
            "!item <ItemName>" : "Show lot of information about item on the command.",
            "!storeItems" : "Show store item name and description about items on store.",
            "!storeItem <StoreItemName>" : "Show all information about store item on the command "
        }

    @commands.command()
    async def helps(self, ctx):
        """Helps command"""
        embedHelps = discord.Embed(title="All commands of bot",
                            description="all parameters of commands have undescore instead of space",
                            colour=discord.Colour.from_rgb(240, 128, 128),
                            )
        for command in self.commands:
            embedHelps.add_field(name=command, value=self.commands[command], inline=False)

        embedHelps.set_thumbnail(url="https://cdn.akamai.steamstatic.com/steam/apps/1966720/capsule_616x353.jpg?t=1700231592")

        await ctx.send(embed=embedHelps)

async def setup(bot):
    await bot.add_cog(HelpsCommand(bot))