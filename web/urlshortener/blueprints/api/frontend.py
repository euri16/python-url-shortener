from flask import Blueprint, request, render_template
from urlshortener.lib.helper import api_response

frontend = Blueprint(__name__, 'urlshortener.blueprints.frontend')
CONTENT_TYPE_JSON = "application/json"


@frontend.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    response = []
    return api_response(False, "Success", 200, response)
