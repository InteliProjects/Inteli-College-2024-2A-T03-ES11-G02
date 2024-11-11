from flask import Flask, jsonify, request
from flask_cors import CORS
import clickhouse_connect
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

# Load environment variables
load_dotenv()

# ClickHouse credentials
CLICKHOUSE_HOST = os.getenv("CLICKHOUSE_HOST").strip()
CLICKHOUSE_PORT = os.getenv("CLICKHOUSE_PORT").strip()
CLICKHOUSE_USER = os.getenv("CLICKHOUSE_USER").strip()
CLICKHOUSE_PASSWORD = os.getenv("CLICKHOUSE_PASSWORD").strip()
CLICKHOUSE_DB = os.getenv("CLICKHOUSE_DB", "default").strip()

# Error handling for database connections
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

# Function to connect to ClickHouse
def connect_to_clickhouse():
    try:
        client = clickhouse_connect.get_client(
            host=CLICKHOUSE_HOST,
            port=CLICKHOUSE_PORT,
            username=CLICKHOUSE_USER,
            password=CLICKHOUSE_PASSWORD,
            database=CLICKHOUSE_DB,
            secure=True,
            verify=False
        )
        return client
    except Exception as e:
        raise ConnectionError(f"Error connecting to ClickHouse: {e}")

# Endpoint to fetch data from ClickHouse
@app.route('/clickhouse/query', methods=['POST'])
def query_clickhouse():
    try:
        client = connect_to_clickhouse()
        query = request.json.get('query')
        result = client.query(query)  # This is where the query is executed
        return jsonify(result.result_rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
