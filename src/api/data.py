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

def getMonster():
    monsterName = "Eyeless Dog"
    cursor.execute("SELECT * FROM Monsters WHERE name_monster ILIKE %s", (monsterName,) )
    return(cursor.fetchall())

def getMoon(moonName : str):
    cursor.execute('SELECT * FROM Monsters WHERE name_moon ILIKE %s', (moonName,))
    return(cursor.fetchall())

def getScrap(scrapName : str):
    cursor.execute('SELECT * FROM Monsters WHERE name_scrape ILIKE %s', (scrapName,))
    return(cursor.fetchall())

def getStore(storeName : str):
    cursor.execute('SELECT * FROM Store WHERE name_store ILIKE %s', (storeName,))
    return(cursor.fetchall())

