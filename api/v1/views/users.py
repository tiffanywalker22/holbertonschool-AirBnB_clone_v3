#!/usr/bin/python3
"""User views module"""
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.user import User


@app_views.route('/users', methods=["GET"], strict_slashes=False)
def get_users():
    """Retrieves the list of all User objects"""
    users = [user.to_dict()
                 for user in storage.all(User).values()]
    return jsonify(users)


@app_views.route('/users/<user_id>',
                 methods=["GET"], strict_slashes=False)
def get_user(user_id):
    """Retrieves a User object"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>',
                 methods=["DELETE"], strict_slashes=False)
def delete_user(user_id):
    """Deletes a User object"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=["POST"], strict_slashes=False)
def create_user():
    """Creates a user"""
    data = request.get_json(silent=True)
    if data is None:
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    if "name" not in data:
        return make_response(jsonify({"error": "Missing name"}), 400)

    new_user = User(**data)
    new_user.save()
    return make_response(jsonify(new_user.to_dict()), 201)


@app_views.route('/users/<user_id>',
                 methods=["PUT"], strict_slashes=False)
def update_user(user_id):
    """Updates a User object"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    data = request.get_json(silent=True)
    if data is None:
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    ignore_list = ["id", "created_at", "updated_at"]
    for key, value in data.items():
        if key not in ignore_list:
            setattr(user, key, value)

    storage.save()
    return make_response(jsonify(user.to_dict()), 200)
