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
region_cities = {'Tanger-Tetouan-AlHoceima': ['AlHoceima', 'Chefchaouen', 'Ouezzane', 'KsarelKebir', 'Larache', 'Assilah', 'Tetouan', 'Mdiq', 'Fnideq', 'Tanger'],
                'Oriental':['Nador', 'Berkane', 'Oujda', 'Driouch', 'Taourirt', 'Jerada', 'Guercif'],
                'Fes-Meknes':['Taouante', 'Taza', 'MoulayYacoub', 'Fes', 'Meknes', 'Sefrou', 'Ifrane', 'Boulmane'],
                'Rabat-Sale-Kenitra':['Rabat', 'Sale', 'Kenitra', 'Oulmes', 'Rommani', 'Ezzhiliga'],
                'Beni Mellal-Khenifra':['Khenifra', 'KasbaTadla', 'BeniMellal', 'Azilal', 'Demnate'],
                'Casablanca-Settat':['Casablanca', 'Mohammedia', 'ElJadida', 'Oualidia', 'SidiBennour'],
                'Marrakech-Safi':['Marrakech', 'Safi', 'Essaouira'],
                'Draa-Tafilalet':['Midelt', 'Errachidia', 'Erfoud', 'Tinghrir', 'Ouarzazate', 'Zagoura'],
                'Souss-Massa':['Agadir', 'Tiznit', 'Tafraout', 'Taliouine', 'Taroudant'],
                'Guelmim-OuedNoun':['SidiIfni', 'Guelmin', 'TanTan'],
                'Laayoune-SaguiaalHamra':['Laayoune', 'Essamara', 'Tarfaya', 'Boujdour'],
                'Dakhla-OuedEdDahab':['Dakhla', 'Lagouira']}

all_objects = storage.all(Region)

for object, value in all_objects.items():
    print(value.name)
    if value.name in region_cities.keys():
        print("-----{}-----".format(value.id))
        for city in region_cities[value.name]:
            print(city)
    print("*****************")