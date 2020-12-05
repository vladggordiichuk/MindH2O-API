from Routes.flask import app
from api_response import data_to_response
from secrets import token_urlsafe

@app.route("/users/register", methods=['POST'])
def api_post_users_register():
    return data_to_response(True, token_urlsafe(16))

@app.route("/users/login", methods=['POST'])
def api_post_users_login():
    return data_to_response(True, token_urlsafe(16))

@app.route("/users/logout", methods=['POST'])
def api_post_users_logout():
    return data_to_response(True, token_urlsafe(16))
