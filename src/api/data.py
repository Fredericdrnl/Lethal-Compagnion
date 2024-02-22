import psycopg2
from dotenv import load_dotenv
import os
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '..\db\.env')
load_dotenv(dotenv_path)


# authentification
conn = psycopg2.connect(database=os.getenv('DB_NAME'),
                        host=os.getenv('DB_HOST'),
                        user=os.getenv('DB_USER'),
                        password=os.getenv('DB_PASSWORD'),
                        port=os.getenv('DB_PORT')
                        )

cursor = conn.cursor()


def getMonsters():
    """
    Get all monsters name of Monsters table.
    """
    cursor.execute("SELECT * FROM Monsters")
    return(cursor.fetchall())

def getMonster(monsterName : str):
    """
    Get all tuple of a monster.

    Args:
        monsterName (str) : Monster which want to get information.
    """
    cursor.execute("SELECT * FROM Monsters WHERE underscore ILIKE %s", (monsterName,))
    return(cursor.fetchall())

def getMoons():
    """
    Get all moons name of Moons table.
    """
    cursor.execute('SELECT * FROM Moons')
    return(cursor.fetchall())

def getMoon(moonName : str):
    """
    Get all tuple of a moon.

    Args:
        moonName (str) : Moon which want to get information.
    """
    cursor.execute('SELECT * FROM Moons WHERE name_moon ILIKE %s', (moonName,))
    return(cursor.fetchall())

def getItems():
    """
    Get all items name of Scraps table.
    """
    cursor.execute("SELECT * FROM Scrap")
    return(cursor.fetchall())

def getItem(itemName : str):
    """
    Get all tuple of a item.

    Args:
        itemName (str) : Item which want to get information.
    """
    cursor.execute("SELECT * FROM scrap WHERE underscore ILIKE %s", (itemName,))
    return(cursor.fetchall())

def getStoreItems():
    """
    Get all store items name of Store table.
    """
    cursor.execute('SELECT * FROM Store')
    return(cursor.fetchall())

def getStoreItem(storeItemName : str):
    """
    Get all tuple of a store item.

    Args:
        storeItemName (str) : Store item which want to get information.
    """
    cursor.execute('SELECT * FROM Store WHERE name_store ILIKE %s', (storeItemName,))
    return(cursor.fetchall())

# if __name__ == "__main__":
#     print(getItem('Yield_Sign'))