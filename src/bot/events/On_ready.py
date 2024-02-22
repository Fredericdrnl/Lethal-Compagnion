from discord.ext import commands
import discord

class On_ReadyEvent(commands.Cog):
    """
    This class create On_ready event
    this event trigger when the bot started.
    """
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("[INFO] Bot is ready !")

async def setup(bot):
    await bot.add_cog(On_ReadyEvent(bot))