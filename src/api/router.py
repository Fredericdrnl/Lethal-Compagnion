import flask
from data import getMonster

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def acceuil():
    return "API du bot discord Lethal Compagny"

@app.route('/Monsters/<str:MonsterName>', methods=['GET'])
def Monsters(MonsterName : str):
    return getMonster(MonsterName)

# @app.route('/Monsters/test', methods=['GET'])
# def Monsters():
#     return getMonster()

if __name__ == "__main__":
    app.run(debug=True)