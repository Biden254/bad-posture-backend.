from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from .routes import main
    app.register_blueprint(main)

    return app
# This function creates and configures the Flask application.
# It initializes the application with CORS support and registers the main blueprint for routing.