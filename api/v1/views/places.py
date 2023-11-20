#!/usr/bin/python3
"""Place views module"""
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.place import Place
from models.city import City
from models.user import User


@app_views.route('/cities/<city_id>/places', methods=["GET"],
                 strict_slashes=False)
def get_places_by_city(city_id):
    """Retrieves the list of all Place objects of city"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    places = [place.to_dict() for place in city.places]
    return jsonify(places)

@app_views.route('/places/<place_id>',
                 methods=["GET"], strict_slashes=False)
def get_place(place_id):
    """Retrieves a Place object"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())



@app_views.route('/places/<place_id>',
                 methods=["DELETE"], strict_slashes=False)
def delete_place(place_id):
    """Deletes a Place object"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/cities/<city_id>/places',
                 methods=["POST"], strict_slashes=False)
def create_place(city_id):
    """Creates a place"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    data = request.get_json(silent=True)
    if data is None:
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    if "user_id" not in data:
        return make_response(jsonify({"error": "Missing user_id"}), 400)

    if User is None:
        abort(404)

    if "name" not in data:
        return make_response(jsonify({"error": "Missing name"}), 400)

    new_place = Place(**data)
    new_place.save()
    return make_response(jsonify(new_place.to_dict()), 201)


@app_views.route('/places/<place_id>',
                 methods=["PUT"], strict_slashes=False)
def update_place(place_id):
    """Updates a Place object"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    data = request.get_json(silent=True)
    if data is None:
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    ignore_list = ["id", "created_at", "updated_at", "user_id", "city_id"]
    for key, value in data.items():
        if key not in ignore_list:
            setattr(place, key, value)

    storage.save()
    return make_response(jsonify(place.to_dict() or {}), 200)
