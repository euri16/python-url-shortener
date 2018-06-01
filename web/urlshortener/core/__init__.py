import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache
from flask.ext.bootstrap import Bootstrap
import redis
import logging
from logging.handlers import RotatingFileHandler
import sys
import traceback

app = Flask(__name__, static_url_path='/../static', template_folder='../templates')
app.root_path = os.path.join(os.path.dirname(__file__))
app.config.from_pyfile("config/production.py", silent=True)
app.db = db = SQLAlchemy(app)
app.cache = cache = Cache(app)
Bootstrap(app)


@app.before_first_request
def setup_logging():  # pragma: no cover
    if not app.debug:
        # In production mode, add log handler to sys.stderr.
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)


def get_redis_client():
    app.logger.debug('lel')
    host = app.config['CACHE_REDIS_HOST']
    port = app.config['CACHE_REDIS_PORT']
    # password = app.config['']
    # db = app.config[]
    redis_client = redis.Redis(host=host, port=port, db=0)
    return redis_client


app.redis = get_redis_client()
