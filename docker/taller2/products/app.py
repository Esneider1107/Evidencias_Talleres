import os
from flask import Flask, jsonify

app = Flask(__name__)
INSTANCE = os.getenv("INSTANCE", "products-1")

@app.get("/")
def home():
    return jsonify({
        "service": "products",
        "message": "Servicio de productos",
        "instance": INSTANCE
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)