from data import *
import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def accueil():
    return "API du bot discord Lethal Company"

# ■■■■■■■■■■■■■■■■■■■■■■■ Monster ■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
@app.route('/Monsters/<MonsterName>', methods=['GET'])
def Monster(MonsterName : str):
    return getMonster(MonsterName)

@app.route('/Monsters/', methods=['GET'])
def Monsters():
    return getMonsters()

# ■■■■■■■■■■■■■■■■■■■■■■■ Moon ■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
@app.route('/Moons/<MoonName>', methods=['GET'])
def Moon(MoonName : str):
    return getMoon(MoonName)

@app.route('/Moons/', methods=['GET'])
def Moons():
    return getMoons()

# ■■■■■■■■■■■■■■■■■■■■■■■ Item ■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
@app.route('/Items/<ItemName>', methods=['GET'])
def Item(ItemName : str):
    return getItem(ItemName)

@app.route('/Items/', methods=['GET'])
def Items():
    return getItems()

# ■■■■■■■■■■■■■■■■■■■■■■■ Store Item ■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
@app.route('/StoreItems/<StoreItemName>', methods=['GET'])
def StoreItem(StoreItemName):
    return getStoreItem(StoreItemName)

@app.route('/StoreItems/', methods=['GET'])
def StoreItems():
    return getStoreItems()

if __name__ == "__main__":
    app.run(debug=True)