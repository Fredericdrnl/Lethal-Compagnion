import flask
from model.data import *

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def acceuil():
    return "API du bot discord Lethal Compagny"

@app.route('/Monsters/<str:MonsterName>', methods=['GET'])
def Monsters(MonsterName : str):
    return getMonster(MonsterName)

if __name__ == "__main__":
    app.run(debug=True)