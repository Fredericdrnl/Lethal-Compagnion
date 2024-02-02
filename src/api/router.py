import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def acceuil():
    return "API du bot discord Lethal Compagny"

if __name__ == "__main__":
    app.run(debug=True)