#!/usr/bin/python3
from flask import Flask, Blueprint, render_template
from models import Storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_appcontext():
    """Close the storage when the application context ends."""
    storage.close()

if __name__ == '__main__':
    app.run(host=HBNB_API_HOST, Port=HBNB_API_PORT, debug=True, threaded=True)