#!/usr/bin/python3
"""Main script for running the Flask application."""

from flask import Flask
from api.v1.views import app_views
from models import storage
import os


app = Flask(__name__)
app.register_blueprint(app_views)

# app.teardown closes the application


@app.teardown_appcontext
def teardown_appcontext(close):
    """Close the storage when the application context ends."""
    storage.close()

# Set the host and port based on environment variables or use default values


if __name__ == '__main__':
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
