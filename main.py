
from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

@app.route("/api/live-coupons")
def get_live_coupons():
    # Simulated Flipp-like logic (mock for now)
    coupons = [
        {"brand": "Colgate", "discount": "$1.50 off", "expires": "2025-06-08"},
        {"brand": "General Mills", "discount": "$2 off", "expires": "2025-06-12"},
        {"brand": "Tide", "discount": "$3 off", "expires": "2025-06-10"},
    ]
    return jsonify(coupons)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
