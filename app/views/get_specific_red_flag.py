"""initialising flask"""
from flask import Flask, request, jsonify


app = Flask(__name__)

red_flag = []


@app.route('/api/v1/red-flags/<int:red_flag_id>', methods=['GET'])
def get_specific_red_flag(red_flag_id):
    flags = [flag for flag in red_flag if flag["id"] == red_flag_id]
    return jsonify(
        {
            'status': 200,
            'data': flags
        }
    ), 200
