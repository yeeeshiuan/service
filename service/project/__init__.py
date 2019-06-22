# project/__init__.py


import os

from flask import Flask
from flask_cors import CORS

# global variable
apiDict = {"thermalPowerGenerationCO2": "https://quality.data.gov.tw/dq_download_json.php?nid=29947&md5_url=9ddc3290bbec618eadd9f53869acf542", 
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
