# -*- coding: utf-8 -*-
"""
Created on 2016/8/15

@author: wb-zy184129
"""
from .app import api_bp
from ..exceptions import ValidationError
from flask import jsonify


def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.stats_code = 403
    return response


def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.stats_code = 401
    return response


@api_bp.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
