# project/__init__.py


import os

from flask import Flask
from flask_cors import CORS

# global variable
apiDict = {"thermalPowerGenerationCO2": "http://data.taipower.com.tw/opendata/apply/file/d061002/%E5%8F%B0%E7%81%A3%E9%9B%BB%E5%8A%9B%E5%85%AC%E5%8F%B8_%E7%81%AB%E5%8A%9B%E7%99%BC%E9%9B%BB_%E6%BA%AB%E5%AE%A4%E6%B0%A3%E9%AB%94%E6%8E%92%E6%94%BE%E9%87%8F.csv", 
           "error": "http://www.google.com/5566"}

# instantiate the extensions


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions

    # register blueprints
    from project.api.base import base_blueprint
    app.register_blueprint(base_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app}

    return app
