from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api')
def api():
    response = jsonify({'message': 'Hello from Python!'})
    return response
