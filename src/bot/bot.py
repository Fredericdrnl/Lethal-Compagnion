from discord.ext import commands
import os

print("[INFO] Launching bot...")

class LethalCompagnion(commands.Bot):
    """
    This class create the discord bot.
    """
    def __init__(self, intents, prefix = "!"):
        commands.Bot.__init__(self, command_prefix=prefix, intents = intents)

    async def setup_hook(self):
        """
        This function load all commands and events of the discord bot.
        """
        print("====== EVENTS ======")
        for fils in os.listdir("./src/bot/events"):
            if fils.endswith(".py"):
                await self.load_extension("events." + fils[:-3])
                print(fils[:-3] + " event is UP !")

        
        print("====== COMMANDS ======")
        for fils in os.listdir("./src/bot/commands"):
            if fils.endswith(".py"):
                await self.load_extension("commands." + fils[:-3])
                print(fils[:-3] + " event is UP !")
