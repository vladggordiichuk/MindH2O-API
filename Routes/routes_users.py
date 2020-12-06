from flask import request

from Routes.flask import app
from Extensions.request_simplifier import data_to_response, get_auth_token

import DataBase.database_requests as db


@app.route("/users/register", methods=['POST'])
def api_post_users_register():

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')

    if first_name is None:
        return data_to_response(False, None, 'Parameter first_name is missing'), 403

    if last_name is None:
        return data_to_response(False, None, 'Parameter last_name is missing'), 403

    if email is None:
        return data_to_response(False, None, 'Parameter email is missing'), 403

    if password is None:
        return data_to_response(False, None, 'Parameter password is missing'), 403

    if db.is_user_registered(email):
        return data_to_response(False, None, 'User is already registered'), 403
    else:
        user = db.save_user_to_database(first_name, last_name, email, password)
        user_dict = user.as_dict()
        user_dict['user_auth'] = db.create_user_auth(user).as_dict()
        return data_to_response(True, user_dict)


@app.route("/users/login", methods=['POST'])
def api_post_users_login():

    email = request.form.get('email')
    password = request.form.get('password')

    if email is None:
        return data_to_response(False, None, 'Parameter email is missing'), 403

    if password is None:
        return data_to_response(False, None, 'Parameter password is missing'), 403

    user = db.get_user_by_email_and_password(email, password)

    if user is not None:
        user_dict = user.as_dict()
        user_dict['user_auth'] = db.create_user_auth(user).as_dict()
        return data_to_response(True, user_dict)
    else:
        return data_to_response(False, None, 'User not found'), 404


@app.route("/users/logout", methods=['POST'])
def api_post_users_logout():
    auth_token = get_auth_token(request.headers.get('Authorization'))
    user = db.check_user_token(auth_token)

    if user is not None:
        db.remove_user_auth(auth_token)
        return data_to_response(True, None, 'User was logged out')
    else:
        return data_to_response(False, None, 'Token not found'), 401


@app.route("/users/me", methods=['GET'])
def api_get_users_me():
    auth_token = get_auth_token(request.headers.get('Authorization'))
    user = db.check_user_token(auth_token)

    if user is not None:
        return data_to_response(True, user.as_dict())
    else:
        return data_to_response(False, None, 'Unauthorized'), 401


@app.route("/users/settings", methods=['POST'])
def api_get_users_settings():
    auth_token = get_auth_token(request.headers.get('Authorization'))
    user = db.check_user_token(auth_token)

    daily_activity_minutes = request.form.get('daily_activity_minutes')
    body_weight_grams = request.form.get('body_weight_grams')

    if daily_activity_minutes is None:
        return data_to_response(False, None, 'Parameter daily_activity_minutes is missing'), 403

    if body_weight_grams is None:
        return data_to_response(False, None, 'Parameter body_weight_grams is missing'), 403

    if user is not None:
        user_settings = db.update_user_settings(user, daily_activity_minutes, body_weight_grams)
        return data_to_response(True, user_settings.as_dict())
    else:
        return data_to_response(False, None, 'Unauthorized'), 401
