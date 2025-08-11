from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/", methods=["GET"])
def home():
    return "Spam Detection API is Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    if not data or "message" not in data:
        return jsonify({"error": "Provide JSON with a 'message' field"}), 400

    msg = data["message"]
    pred = int(model.predict([msg])[0])
    return jsonify({"prediction": "spam" if pred == 1 else "ham", "label": pred})

if __name__ == "__main__":
    app.run(debug=True)
