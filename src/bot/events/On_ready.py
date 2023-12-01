from discord.ext import commands
import discord

class On_ReadyEvent(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("[INFO] Bot is ready !")

def setup(bot):
    bot.add_cog(On_ReadyEvent(bot))