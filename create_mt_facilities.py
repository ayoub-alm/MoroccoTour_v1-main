#!/usr/bin/python3
"""
 create different morocco tourism categories
"""
from models import storage
from models.regions import Region
from models.cities import City
from models.categories import Category
from models.facilities import Facility


list_facilities = ['Guided Tours',
                   'Historical Exhibits and Information',
                   'Cafes and Restaurants',
                   'Restrooms',
                   'Picnic Areas',
                   'Shopping',
                   'Water Sports and Equipment Rentals',
                   'Hiking Trails',
                   'Local Accommodations',
                   'Cultural and Educational Programs',
                   'Spa and Wellness Services',
                   'Camping Areas',
                   'Scenic Viewpoints',
                   'Art and Craft Workshops',
                   'Health and Wellness Treatments']


for item in list_facilities:
    new_facility = Facility(name=item)
    new_facility.save()
    print(new_facility.name)

print("facilities added succefully!!!!")