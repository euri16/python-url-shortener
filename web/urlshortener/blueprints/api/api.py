from flask import Blueprint
from urlshortener.lib.helper import api_response

api = Blueprint(__name__, 'urlshortener.blueprints.api')
CONTENT_TYPE_JSON = "application/json"


@api.route('shorten_url', methods=['POST'])
def shorten_url():
    response = []
    return api_response(False, "Success", 200, response)
