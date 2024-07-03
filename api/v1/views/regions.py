#!/usr/bin/python3
"""region views module"""
from api.v1.views import app_views
from flask import jsonify
from flask import abort
from flask import request
from models import storage
from models.regions import Region


@app_views.route('/regions', methods=['GET'],
                 strict_slashes=False)
def all_regions():
    """retrieve all regions"""
    all_regions = storage.all(Region)
    list_regions = []
    for obj in all_regions.values():
        list_regions.append(obj.to_dict())
    return jsonify(list_regions)


@app_views.route('/regions/<state_id>', methods=['GET'],
                 strict_slashes=False)
def get_state(state_id):
    """retrive region based on id"""
    all_states = storage.all(Region)
    for obj in all_states.values():
        if obj.id == state_id:
            return jsonify(obj.to_dict())
    abort(404)


@app_views.route('/regions/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """delete region"""
    all_states = storage.all(Region)
    for obj in all_states.values():
        if obj.id == state_id:
            storage.delete(obj)
            storage.save()
            return jsonify({}), 200
    abort(404)


@app_views.route('/regions', methods=['POST'],
                 strict_slashes=False)
def create_state():
    """create new region"""
    if request.is_json:
        dict = request.get_json()
        if "name" in dict.keys():
            new_state = Region(**dict)
            new_state.save()
            return jsonify(new_state.to_dict()), 201
        abort(400, "Missing name")
    abort(400, "Not a JSON")


@app_views.route('/regions/<state_id>', methods=['PUT'],
                 strict_slashes=False)
def update_state(state_id):
    """update region"""
    region = storage.get(Region, state_id)
    if region is not None:
        if request.is_json:
            inputs = request.get_json()
            for key, value in inputs.items():
                ignore = ['id', 'created_at', 'updated_at']
                if key not in ignore:
                    setattr(region, key, value)
            region.save()
            return jsonify(region.to_dict()), 200
        abort(400, "Not a JSON")
    abort(404)
