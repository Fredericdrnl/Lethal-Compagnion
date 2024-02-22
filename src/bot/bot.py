from discord.ext import commands
import os

print("[INFO] Launching bot...")

class LethalCompagnion(commands.Bot):
    def __init__(self, intents, prefix = "!"):
        commands.Bot.__init__(self, command_prefix=prefix, intents = intents)

    

    async def setup_hook(self):
        cogs = ['events.On_ready',
            'commands.Item',
            'commands.Items',
            'commands.Monster',   
            'commands.Monsters',
            'commands.Moon',
            'commands.Moons',
            'commands.StoreItem',
            'commands.StoreItems'
        ]

        for cog in cogs:
            await self.load_extension(cog)

        # DON'T WORK WITH DOCKER
        # print("====== EVENTS ======")
        # for fils in os.listdir("./src/bot/events"):
        #     if fils.endswith(".py"):
        #         await self.load_extension("events." + fils[:-3])
        #         print(fils[:-3] + " event is UP !")

        
        # print("====== COMMANDS ======")
        # for fils in os.listdir("./src/bot/commands"):
        #     if fils.endswith(".py"):
        #         await self.load_extension("commands." + fils[:-3])
        #         print(fils[:-3] + " event is UP !")
