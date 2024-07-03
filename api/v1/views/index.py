#!/usr/bin/python3
"""index views module"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.regions import Region
from models.cities import City
from models.facilities import Facility
from models.places import Place
from models.reviews import Review
from models.users import User
from models.categories import Category


@app_views.route('/status', methods=['GET'])
def get_status():
    """return status ok"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def stats_count():
    """return number of each object"""
    classes = {"facilities": Facility, "cities": City, "places": Place,
               "reviews": Review, "regions": Region,
               "users": User, "categories": Category}
    counts = {}
    for key, obj in classes.items():
        counts[key] = storage.count(obj)
    return jsonify(counts)
