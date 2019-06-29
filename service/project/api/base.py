# project/api/base.py


from flask import Blueprint, jsonify, request
import requests, json, csv, sys

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
    print(key)
    if key in apiDict:

        res = requests.get(apiDict[key])

        status = "success"
        message = "Resource problem."

        if res.status_code == 200:
            text=res.iter_lines(decode_unicode='utf-8')
            reader=csv.reader(text,delimiter=',')
            message = json.dumps( [ row for row in reader ] )
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

@base_blueprint.route('/base/normalAPI',methods=['POST'])
def normalAPI():
    post_data = request.get_json()

    response_object = {
        'status': 'fail',
        'message': 'Invalid payload.'
    }

    if not post_data:
        return jsonify(response_object), 400

    url = post_data.get('url')

    res = requests.get(url)

    status = "success"
    message = "Resource problem."

    if res.status_code == 200:
        if url[-3:] == "csv":
            text=res.iter_lines(decode_unicode='utf-8')
            reader=csv.reader(text,delimiter=',')
            message = json.dumps( [ row for row in reader ] )
        else:
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
