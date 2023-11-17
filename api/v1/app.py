#!/usr/bin/python3
"""Main script for running the Flask application."""

from flask import Flask
from api.v1.views import app_views
from models import storage
from os import getenv
from flask import jsonify


app = Flask(__name__)
app.register_blueprint(app_views)

# app.teardown closes the application


@app.teardown_appcontext
def teardown_appcontext(close):
    """Close the storage when the application context ends."""
    storage.close()


# Set the host and port based on environment variables or use default values
@app.errorhandler(404)
def not_found(error):
    """ 404 error """
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    host = getenv("HBNB_API_HOST", default="0.0.0.0")
    port = getenv("HBNB_API_PORT", default="5000")
    app.run(host=host, port=port, threaded=True)
