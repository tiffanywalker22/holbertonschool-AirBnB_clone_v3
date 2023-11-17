#!/usr/bin/python3
"""Main script for running the Flask application."""

from flask import Flask
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')

# app.teardown closes the application


@app.teardown_appcontext
def teardown_appcontext():
    """Close the storage when the application context ends."""
    storage.close()

# Set the host and port based on environment variables or use default values


host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
port = int(os.environ.get('HBNB_API_PORT', 5000))

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True, threaded=True)
