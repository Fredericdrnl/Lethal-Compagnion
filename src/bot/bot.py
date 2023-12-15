from discord.ext import commands
import os

print("[INFO] Launching bot...")

class LethalCompagnion(commands.Bot):
    def __init__(self, intents, prefix = "!"):
        commands.Bot.__init__(self, command_prefix=prefix, intents = intents)

    async def setup_hook(self):
        print("====== EVENTS ======")
        for fils in os.listdir("./src/bot/events"):
            if fils.endswith(".py"):
                await self.load_extension("events." + fils[:-3])
                print(fils[:-3] + " event is UP !")
