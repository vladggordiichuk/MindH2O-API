from Routes.flask import app
from api_response import data_to_response
from secrets import token_urlsafe

@app.route("/logs", methods=['GET'])
def api_get_logs():
    return data_to_response(True, None)

@app.route("/logs", methods=['POST'])
def api_post_logs():
    return data_to_response(True, token_urlsafe(16))

@app.route("/logs/<int:id>", methods=['DELETE'])
def api_delete_logs(id):
    return data_to_response(True, id)