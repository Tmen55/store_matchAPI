from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Smart Coupon Backend is running!'

# Add this block to bind the port Render expects:
import os
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Render injects PORT env var
    app.run(host='0.0.0.0', port=port)
