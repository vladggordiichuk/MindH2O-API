from Routes.flask import app
from Extensions.request_simplifier import data_to_response

@app.route('/', methods=['GET'])
def api_get_home():
    return '''<h1>Mind H2O API</h1>
<p>To see documentation proceed to
<a href="https://app.swaggerhub.com/apis-docs/vladggordiichuk/MindH2O/1.0.0">Swagger</a>
</p>'''

@app.errorhandler(404)
def page_not_found(e):
    return data_to_response(False, None, "Endpoint not found")