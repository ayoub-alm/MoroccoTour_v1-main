#!/usr/bin/python3
"""
 create some places
"""
from models import storage
from models.places import Place
from models.cities import City
from models.categories import Category



places = [{'name': 'Kasbah Museum',
           'description': 'The Kasbah Museum in Tangier, Morocco, is housed in the former Sultans palace, Dar el-Makhzen. It features exhibits showcasing the region history, culture, and art, including artifacts from the Phoenician, Roman, and Islamic periods. The museum is known for its beautiful Andalusian-style architecture and stunning views of the Strait of Gibraltar',
           'latitude': '35.7904',
           'longitude': '5.8129',
           'city_id': 'Tanger',
           'user_id': '42228493-34d5-45e8-8cb1-a2a8dab5d114',
           'categorie_id': 'Cultural Tourism'},
           {'name': 'Outa el Hammam',
           'description': 'Outa el Hammam Square in Chefchaouen, Morocco, is the vibrant heart of the city, surrounded by cafes, restaurants, and shops. It offers a lively atmosphere and stunning views of the surrounding blue-painted buildings. The square is also home to the historic Grand Mosque and the Kasbah, making it a central hub for both locals and visitors.',
           'latitude': '35.1686',
           'longitude': '5.2639',
           'city_id': 'Chefchaouen',
           'user_id': '42228493-34d5-45e8-8cb1-a2a8dab5d114',
           'categorie_id': 'Cultural Tourism'}]

#cities_ids
list_cities = storage.all(City)
cities_ids = {}
for object, value in list_cities.items():
    cities_ids[value.name] = value.id


#categories_ids
list_categories = storage.all(Category)
cat_ids = {}
for object, value in list_categories.items():
    cat_ids[value.name] = value.id


