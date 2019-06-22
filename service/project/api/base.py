# project/api/base.py


from flask import Blueprint, jsonify
import requests, json

from project import apiDict
from project.api.utils import authenticate


base_blueprint = Blueprint('base', __name__)


@base_blueprint.route('/base/pingAuth', methods=['GET'])
@authenticate
def ping_pongauth(resp):
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

@base_blueprint.route('/base/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

@base_blueprint.route('/base/api/<key>',methods=['GET'])
def api(key):

    if key in apiDict:

        res = requests.get(apiDict[key])

        status = "success"
        message = "Resource problem."

        if res.status_code == 200:
            try:
                message = res.json()
            except json.decoder.JSONDecodeError:
                status = "fail"
                message = "Can not decoder data to json."
        else:
            status = "fail"

        return jsonify({
            'status': status,
            'message': message
        }), 200
    else:
        return jsonify({
            'status': 'fail',
            'message': f"Your key doesn't support!({key})"
        }), 404
