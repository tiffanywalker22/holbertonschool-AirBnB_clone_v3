#!/usr/bin/python3
"""Run this script to start the Flask application and
expose the '/status' endpoint."""
from api.v1.views import app_views
from models import storage
from flask import jsonify



@app_views.route('/status', methods=['GET'])
def get_status():
    """Handle GET request to the /status endpoint.

    Returns:
        Response: JSON response with status "OK".
    """
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'])
    def get_stats():
        """ Retrieves stats of each obj by type """
        classes = {
            "amenities": "Amenity",
            "cities": "City",
            "places": "Place",
            "reviews": "Review",
            "states": "State",
            "users": "User"
        }
        return jsonify(classes)
