from flask import Flask
from config import config

from flask_cors.extension import CORS


def create_app(config_name):
    app = Flask(__name__)
    CORS(app,
         supports_credentials=True,
         origins=[
             'http://localhost:8000',
         ])
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
