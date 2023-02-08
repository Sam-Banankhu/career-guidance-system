from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

@app.route("/")
def root():
    return "Hello, World"

@app.route("/predict", methods=["POST"])
def predict():
    # load your machine learning model
    model = pickle.load(open("model.pkl", "rb"))
    # get data from the request
    data = request.get_json()["data"]
    # make predictions
    prediction = model.predict(data)
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(port=9000)
