#!/usr/bin/python3
"""Run this script to start the Flask application and expose the '/status' endpoint."""
from api.v1.views import app_views
from flask import jsonify



@app_views.route('/status', methods=['GET'])
def get_status():
    """Handle GET request to the /status endpoint.

    Returns:
        Response: JSON response with status "OK".
    """
    return jsonify({"status": "OK"})


if __name__ == '__main__':
    from app import app
    app.run(host='0.0.0.0', port=5000)
