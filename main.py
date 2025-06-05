from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/flipp")
def scrape_flipp():
    try:
        url = "https://flipp.com/en-us"  # Example target
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Simulated scrape logic (replace with real selectors)
        coupons = [
            {"brand": "Tide", "offer": "$3 Off", "expires": "2025-06-10"},
            {"brand": "Colgate", "offer": "$1.50 Off", "expires": "2025-06-08"},
        ]
        return jsonify(coupons)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
