#!/usr/bin/python3
from flask import Blueprint
from api.v1.views.index import *

app_views.register_blueprint(app_views, url_prefix='/api/v1)')
