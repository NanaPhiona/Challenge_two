from flask import Flask, request, jsonify


app = Flask(__name__)

red_flag = []

@app.route('/api/v1/red-flags/<int:red_flag_id>', methods=['DELETE'])
def delete_specific_red_flag(red_flag_id):
    flags = [flag for flag in red_flag if flag["id"] == red_flag_id]
    red_flag.remove(flags[0])
    return jsonify(
        {
            'status': 202,
            'data': [{
                'id': red_flag_id,
                'message': "red-flag record has been deleted"
            }]
        }
    ), 202
