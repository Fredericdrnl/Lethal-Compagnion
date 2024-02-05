import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(database=os.getenv('DB_NAME'),
                        host=os.getenv('DB_HOST'),
                        user=os.getenv('DB_USER'),
                        password=os.getenv('DB_PASSWORD'),
                        port=os.getenv('DB_PORT')
                        )

cursor = conn.cursor()


def getMonster(monsterName : str):
    cursor.execute("SELECT * FROM Monsters WHERE name_monster ILIKE ?", monsterName)

def getMoon(moonName : str):
    cursor.execute("SELECT * FROM Monsters WHERE name_moon ILIKE ?", moonName)

def getScrap(scrapName : str):
    cursor.execute("SELECT * FROM Monsters WHERE name_scrape ILIKE ?", scrapName)

def getStore(storeName : str):
    cursor.execute("SELECT * FROM Store WHERE name_store ILIKE ?", storeName)

