from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def receive_data():
    data = request.json
    print('Received data:', data)
    return jsonify({'status': 'success', 'data': data})

if __name__ == '__main__':
    app.run(port=5000)

