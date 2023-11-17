#!/usr/bin/python3
from flask import Blueprint


app_views.register_blueprint(app_views, url_prefix='/api/v1)')
# Import specific names or use aliases
from api.v1.views.index import function1, function2