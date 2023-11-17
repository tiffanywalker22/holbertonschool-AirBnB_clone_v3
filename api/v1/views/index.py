#!/usr/bin/python3
"""Run this script to start the Flask application and
expose the '/status' endpoint."""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def get_status():
    """Handle GET request to the /status endpoint.

    Returns:
        Response: JSON response with status "OK".
    """
    return jsonify({"status": "OK"})

@app_views.route('/stats')
    def get_stats():
        """"""
    classes = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    return jsonify(classes)
