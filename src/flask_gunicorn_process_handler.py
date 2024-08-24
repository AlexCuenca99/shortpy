""" This module defines the main entry for the app

    As we are using Gunicorn for raise the app, we need to define the 
    app as a variable which will be passed to docker-compose main CMD 
    for initialize the app
"""

# Blueprints
from src.app.controllers.urls_controller import create_urls_blueprints_v1

# Locals
# Flask app
from src.app.flask_mysql.create_flask_mysql_app import create_flask_mysql_app

blueprints = []

blueprints.append(create_urls_blueprints_v1())

app = create_flask_mysql_app(blueprints=blueprints)
