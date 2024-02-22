import os
from os.path import join, dirname
import discord
import asyncio
from dotenv import load_dotenv

from bot import LethalCompagnion

dotenv_path = join(dirname(__file__), '..\db\.env')
load_dotenv(dotenv_path)

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