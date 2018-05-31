from urlshortener.core import app
from flask import make_response, render_template
from urlshortener.blueprints.api import ACTIVE as active_blueprints
import os

for url, blueprint in active_blueprints:
    app.register_blueprint(blueprint, url_prefix=url)
    app.static_folder = os.path.join(
        os.path.realpath(os.path.dirname(__file__)), "static")


@app.errorhandler(429)
def abuse_error_handler(e):
    response = make_response(render_template('abuse.html'), 429)
    return response


if __name__ == '__main__':
    app.run()
