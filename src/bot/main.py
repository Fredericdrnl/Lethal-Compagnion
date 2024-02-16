import os
import discord
from bot import LethalCompagnion
import asyncio
from dotenv import load_dotenv

load_dotenv() 

class Main():
    @staticmethod
    def run():
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        try:
            token = open(os.path.join(__location__, ".env"), "r").read().strip("\n")
        except FileNotFoundError:
            quit("Please create a .env file and place your token in 'DISC_TOKEN' files!")
        if token is None:
            quit("Please create a .env file and place your token in 'DISC_TOKEN' files!")
        else:
            intent = discord.Intents.all()
            intent.members = True
            intent.message_content = True
            bot = LethalCompagnion(intent)
            bot.run(os.getenv("DISC_TOKEN"))

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(Main.run())