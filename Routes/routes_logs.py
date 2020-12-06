from flask import request

from Routes.flask import app
from Extensions.request_simplifier import data_to_response, get_auth_token

import DataBase.database_requests as db


@app.route("/logs", methods=['GET'])
def api_get_logs():
    auth_token = get_auth_token(request.headers.get('Authorization'))
    user = db.check_user_token(auth_token)

    if user is not None:
        logs = db.get_logs(user)

        return data_to_response(True, list(map(lambda log: log.as_dict(), logs)))
    else:
        return data_to_response(False, None, 'Unauthorized'), 401


@app.route("/logs", methods=['POST'])
def api_post_logs():
    auth_token = get_auth_token(request.headers.get('Authorization'))
    user = db.check_user_token(auth_token)

    grams = request.form.get('grams')

    if grams is None:
        return data_to_response(False, None, 'Parameter grams is missing'), 403

    if user is not None:
        log = db.add_log(user, grams)
        return data_to_response(True, log.as_dict())
    else:
        return data_to_response(False, None, 'Unauthorized'), 401


@app.route("/logs/<int:id>", methods=['DELETE'])
def api_delete_logs(id):
    auth_token = get_auth_token(request.headers.get('Authorization'))
    user = db.check_user_token(auth_token)

    if user is not None:
        if db.remove_log(user, id):
            return data_to_response(True, None, 'Log was removed')
        else:
            return data_to_response(False, None, 'Log was not found')
    else:
        return data_to_response(False, None, 'Unauthorized'), 401
