"""initialising flask"""
from flask import Flask, request, jsonify


app = Flask(__name__)

red_flag = []

@app.route('/api/v1/red-flags/<int:red_flag_id>/location', methods=['PATCH'])
def edit_specific_red_flags(red_flag_id):
    flags = [flag for flag in red_flag if flag["id"] == red_flag_id]
    flags[0]['location'] = request.json['location']

    if not flags[0]['location']:
        return jsonify(
            {
                'status': 404,
                'error': 'No data'
            }
        ), 404

    if flags is None:
        return jsonify(
            {
                'status': 404,
                'error': 'No data'
            }
        ), 404

    return jsonify(
        {
            'status': 200,
            'data': [{
                'id': red_flag_id,
                'message': "updated red-flag record's location"
            }]
        }
    ), 200
