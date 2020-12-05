from flask import jsonify

def data_to_response(success, data, meessage = None):
    return  jsonify({
        "success": success,
        "data": data,
        "message": meessage
    })