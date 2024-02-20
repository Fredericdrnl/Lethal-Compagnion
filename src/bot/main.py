import os
import discord
from bot import LethalCompagnion
import asyncio
from dotenv import load_dotenv

load_dotenv() 

class Main():
    @staticmethod
    def run():
        intent = discord.Intents.all()
        intent.members = True
        intent.message_content = True
        bot = LethalCompagnion(intent)
        bot.run(os.getenv("DISC_TOKEN"))

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(Main.run())