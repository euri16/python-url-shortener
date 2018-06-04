from flask import Blueprint, request, render_template, redirect
from urlshortener.core import app
from urlshortener.lib.helper import api_response
from urlshortener.lib.IntEncoder import IntEncoder
from urlshortener.models import ShortenedUrl

frontend = Blueprint(__name__, 'urlshortener.blueprints.frontend')
CONTENT_TYPE_JSON = "application/json"

idgen = IntEncoder()

@frontend.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

    long_url = request.form.get('long_url', False)

    shortened_url = ShortenedUrl(long_url)
    app.db.session.add(shortened_url)
    app.db.session.commit()

    encoded_id = idgen.encode(shortened_url.id)
    short_url = '%s%s' % (request.url_root, encoded_id)
    return render_template('index.html', shortUrl=short_url)


@frontend.route('<string:encoded_id>', methods=['GET'])
def process_short_url(encoded_id):
    decoded_id = idgen.decode(encoded_id)

    shortened_url = ShortenedUrl.query.get(decoded_id)
    shortened_url.openings += 1
    app.db.session.add(shortened_url)
    app.db.session.commit()

    return redirect(shortened_url.long_url)


@frontend.route('data/top', methods=['POST', 'GET'])
def topUrls():
    urls = ShortenedUrl.query.filter(ShortenedUrl.openings > 0).order_by(ShortenedUrl.openings.desc()).limit(app.config.get('TOP_URLS_LIMIT')).all()
    app.logger.debug(urls)
    return render_template('top_urls.html', urls=urls, host=request.url_root)