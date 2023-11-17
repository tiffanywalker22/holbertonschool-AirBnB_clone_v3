#!/usr/bin/python3
from flask import jsonify
from api.v1.views import app_views


def get_status():
    """Handle GET request to the /status endpoint.

    Returns:
        Response: JSON response with status "OK".
    """
    return jsonify({"status": "OK"})


"""Attach the route to the app_views Blueprint"""
app_views.add_url_rule('/status', 'get_status', get_status, methods=['GET'])

if __name__ == '__main__':
    from app import app
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
