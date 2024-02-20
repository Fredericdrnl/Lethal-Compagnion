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

def getMonsters():
    cursor.execute("SELECT * FROM Monsters")
    return(cursor.fetchall())

def getMonster(monsterName : str):
    cursor.execute("SELECT * FROM Monsters WHERE underscore ILIKE %s", (monsterName,))
    return(cursor.fetchall())

def getMoons():
    cursor.execute('SELECT * FROM Moons')
    return(cursor.fetchall())

def getMoon(moonName : str):
    cursor.execute('SELECT * FROM Moons WHERE name_moon ILIKE %s', (moonName,))
    return(cursor.fetchall())

def getItems():
    cursor.execute("SELECT * FROM Scrap")
    return(cursor.fetchall())

def getItem(scrapName : str):
    cursor.execute("SELECT * FROM scrap WHERE underscore ILIKE %s", (scrapName,))
    return(cursor.fetchall())

def getStoreItems():
    cursor.execute('SELECT * FROM Store')
    return(cursor.fetchall())

def getStoreItem(storeItemName : str):
    cursor.execute('SELECT * FROM Store WHERE name_store ILIKE %s', (storeItemName,))
    return(cursor.fetchall())

# if __name__ == "__main__":
#     print(getItem('Yield_Sign'))