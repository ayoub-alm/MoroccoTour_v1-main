#!/usr/bin/python3
"""
 create different morocco tourism categories
"""
from models import storage
from models.regions import Region
from models.cities import City
from models.categories import Category


list_categories = ['Cultural Tourism',
                   'Beach and Coastal Tourism',
                   'Nature and Ecotourism',
                   'Shopping and Souvenirs',
                   'Religious and Spiritual Tourism',
                   'Adventure Tourism']

for item in list_categories:
    new_category = Category(name=item)
    new_category.save()
    print(new_category.name)

print("categories added succefully!!!!")