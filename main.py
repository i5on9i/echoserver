"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
import os

import json
from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__, static_url_path='')
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500


@app.route("/spk/json/<path:path>", methods=['POST', 'GET'])
def send_js(path):
    file, ext = os.path.splitext(path)
    if ext == "":
        ext = ".json"

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "json", file + ext)
    s = ''
    with open(json_url) as f:

        for line in f:
            s += line

    return s


if __name__ == '__main__':
    app.run()
