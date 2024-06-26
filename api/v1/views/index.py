#!/usr/bin/python3
'''Index view for the API'''
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Returns JSON """
    return jsonify(status="OK")
