from flask import Flask, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.route("/")
def home():
    logging.info("Home endpoint called")
    return jsonify({"message": "API is running"})

if __name__ == "__main__":
    app.run(debug=True)
