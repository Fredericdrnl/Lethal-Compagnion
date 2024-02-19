import flask
from data import getMonster, getMonsters, getItems, getMoons, getStoreItems

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def acceuil():
    return "API du bot discord Lethal Compagny"

@app.route('/Monsters/test', methods=['GET'])
def Bestiary(MonsterName : str):
    return getMonster(MonsterName)

@app.route('/Monsters/', methods=['GET'])
def Monsters():
    return getMonsters()

@app.route('/Moons/', methods=['GET'])
def Moons():
    return getMoons()

@app.route('/Items/', methods=['GET'])
def Items():
    return getItems()

@app.route('/StoreItems/', methods=['GET'])
def StoreItems():
    return getStoreItems()



if __name__ == "__main__":
    app.run(debug=True)