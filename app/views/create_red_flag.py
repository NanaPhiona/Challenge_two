from flask import Flask, request, jsonify
from app.models.user_model import user
from app.models.red_flag_model import incident



app = Flask(__name__)

user_list = []
red_flag = []


@app.route('/')
def index():
    return jsonify(
        {
            'status': 201,
            'message': "Welcome to iReporter"
        }
    )

@app.route('/api/v1/red-flags', methods=['POST'])
def create_red_flags():
    req = request.json

    if not req:
        return jsonify({
            'status': 404,
            'error': 'No data'
        }), 404

    red_flag.append(req)
    return jsonify({
        'status': 201,
        'data': red_flag
        }), 201