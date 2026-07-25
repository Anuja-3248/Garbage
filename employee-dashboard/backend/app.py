from flask import Flask, jsonify
from flask_cors import CORS
from garbage import process_data

app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return "Employee Dashboard Backend is Running!"


@app.route("/api/data")
def get_data():
    data = process_data()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)