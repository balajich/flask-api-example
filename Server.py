from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/complaint', methods=['POST'])
def foo():
    data = request.json
    data['id'] = 1234
    data['category'] = 'Roads and Building'
    return  data
