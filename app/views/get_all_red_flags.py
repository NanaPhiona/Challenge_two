"""initialising flask"""
from flask import Flask, request, jsonify, Blueprint


app = Flask(__name__)

red_flag = []


@app.route('/api/v1/red-flags', methods=['GET'])
def get_all_red_flags():
    return jsonify(
        {
            'status': 200,
            'data': red_flag
        }
    ), 200
