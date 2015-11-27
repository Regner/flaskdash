

from flask import Flask

# Configuration
from flaskdash.settings import AppConfig
from flaskdash.extensions import configure_extensions

from flaskdash.routes import blueprint

def create_app():
    """ Creates the app. """

    app = Flask(__name__)
    app.config.from_object(AppConfig)

    configure_extensions(app)

    app.register_blueprint(blueprint)

    return app
