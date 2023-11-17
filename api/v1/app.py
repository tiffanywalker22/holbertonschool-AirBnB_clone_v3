#!/usr/bin/python3
"""Main script for running the Flask application."""

from flask import Flask
from api.v1.views import app_views
from models import Storage
import os


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')

# app.teardown closes the application


@app.teardown_appcontext
def teardown_appcontext():
    """Close the storage when the application context ends."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
