#!/usr/bin/python3
"""
 Test cities access from a state
"""
from models import storage
from models.regions import Region
from models.cities import City
from models.categories import Category

"""
 Region Objects creations
"""

list_regions =['Tanger-Tetouan-AlHoceima',
               'Oriental',
               'Fes-Meknes',
               'Rabat-Sale-Kenitra',
               'Beni Mellal-Khenifra',
               'Casablanca-Settat',
               'Marrakech-Safi',
               'Draa-Tafilalet',
               'Souss-Massa',
               'Guelmim-OuedNoun',
               'Laayoune-SaguiaalHamra',
               'Dakhla-OuedEdDahab']

for item in list_regions:
    region = Region(name=item)
    region.save()
    print(region)
