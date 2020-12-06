from flask import jsonify


def data_to_response(success, data, meessage = None):
    return jsonify({
        "success": success,
        "data": data,
        "message": meessage
    })


def get_auth_token(authorization):

    if authorization is not None:
        return authorization.split(" ")[1]
    else:
        return None
