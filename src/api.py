from flask import Flask, Response, request
import pandas as pd
import os
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

training_data = pd.read_csv(os.path.join("data/auto-mpg-training-data.csv"))

# Modell laden
file_to_open = open(os.path.join("data/models/regression.pickle"), "rb")
trained_model = pickle.load(file_to_open)
file_to_open.close ()

# Ausgaben in Browser mit wsgi erzeugen
@app.route("/", methods=["GET"])
def index():
    return {"message": "hello, world"}

@app.route("/hello_world", methods=["GET"])
def hello_world():
    return ("<p>Hello World!<p>")

@app.route("/training_data", methods=["GET"])
def get_training_data():
    return Response(training_data.to_json(), mimetype="application/json")

@app.route("/predict", methods=["GET"])
def predict():
    zylinder = float(request.args.get("zylinder"))
    ps = float(request.args.get("ps"))
    gewicht = float(request.args.get("gewicht"))
    beschleunigung = float(request.args.get("beschleunigung"))
    baujahr = float(request.args.get("baujahr"))

    if (zylinder and ps and gewicht and beschleunigung and baujahr):
        prediction = trained_model.predict([[zylinder, ps, gewicht, beschleunigung, baujahr]])
        return {"result": prediction [0]}
    else:
        return Response ("Please provide all necessary parameters to get a prediction", mimetype="application/json")



