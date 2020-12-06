from Routes.flask import app

import Routes.routes_general
import Routes.routes_users
import Routes.routes_logs

if __name__ == '__main__':
    app.run(debug=True)