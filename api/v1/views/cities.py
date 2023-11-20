#!/usr/bin/python3
"""City views module"""
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.city import City
from models.state import State


@app_views.route('/states/<state_id>/cities',
                 methods=["GET"], strict_slashes=False)
def get_cities_by_state(state_id):
    """Retrieves the list of all City objects of a State"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)


@app_views.route('/cities/<city_id>', methods=["GET"], strict_slashes=False)
def get_city(city_id):
    """Retrieves a City object"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=["DELETE"], strict_slashes=False)
def delete_city(city_id):
    """Deletes a City object"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states/<state_id>/cities',
                 methods=["POST"], strict_slashes=False)
def create_city(state_id):
    """Creates a City"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    data = request.get_json(silent=True)
    if data is None:
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    if "name" not in data:
        return make_response(jsonify({"error": "Missing name"}), 400)

    new_city = City(name=data["name"], state_id=state_id)
    new_city.save()
    return make_response(jsonify(new_city.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=["PUT"], strict_slashes=False)
def update_city(city_id):
    """Updates a City object"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    data = request.get_json(silent=True)
    if data is None:
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    ignore_list = ["id", "state_id", "created_at", "updated_at"]
    for key, value in data.items():
        if key not in ignore_list:
            setattr(city, key, value)

    storage.save()
    return make_response(jsonify(city.to_dict()), 200)
