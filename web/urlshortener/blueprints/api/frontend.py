from flask import Blueprint, request, render_template
from urlshortener.core import app
from urlshortener.lib.helper import api_response
from urlshortener.lib.IntEncoder import IntEncoder

frontend = Blueprint(__name__, 'urlshortener.blueprints.frontend')
CONTENT_TYPE_JSON = "application/json"

@frontend.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        idgen = IntEncoder()
        encoded = idgen.encode(210)

        app.logger.debug(encoded)
        app.logger.debug(idgen.decode(encoded))
    
        return render_template('index.html')
    response = []
    return api_response(False, "Success", 200, response)
