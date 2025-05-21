from flask import Blueprint, jsonify, request
from joblib import load
import json
import os

api_bp = Blueprint("api", __name__, url_prefix="/api")

# File paths
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, 'data')
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')

# Load trained model
model = load(MODEL_PATH)

@api_bp.route("/threats")
def get_threats():
    with open(os.path.join(DATA_DIR, 'threat_data.json')) as f:
        data = json.load(f)
    return jsonify(data)

@api_bp.route("/route")
def get_route():
    coords = [
        {"lat": 12.9, "lng": 80.1},
        {"lat": 13.0, "lng": 80.2},
        {"lat": 13.1, "lng": 80.3},
        {"lat": 13.2, "lng": 80.4}
    ]
    return jsonify(coords)

@api_bp.route("/route-nodes")
def get_route_nodes():
    return jsonify(["A", "B", "C", "D"])

@api_bp.route("/predict", methods=["POST"])
def predict_threat_level():
    try:
        data = request.get_json()
        features = [[
            float(data["lat"]),
            float(data["lng"]),
            float(data["velocity"]),
            float(data["heading"])
        ]]
        risk_score = model.predict(features)[0]
        return jsonify({"risk_score": float(risk_score)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@api_bp.route("/")  # Root endpoint
def health():
    return "Backend is alive."
