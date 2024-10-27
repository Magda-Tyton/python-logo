from flask import Flask

from .routes import main


def create_app() -> Flask:
    """Creates and configures the Flask application.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    app.register_blueprint(main)
    return app
