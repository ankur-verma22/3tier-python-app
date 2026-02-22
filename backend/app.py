from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "3-Tier App Running 🚀"})

@app.route("/db")
def db_check():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database="postgres",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    return jsonify({"db_status": "Connected ✅"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
