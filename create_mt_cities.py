#!/usr/bin/python3
"""
 Test cities access from a state
"""
from models import storage
from models.regions import Region
from models.cities import City
from models.categories import Category

"""
 City Objects creations
"""

# this script should be executed after regions creation
# please change the id of region after regions creation
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

all_regions = storage.all(Region)

for object, value in all_regions.items():
    if value.name in region_cities.keys():
        for city in region_cities[value.name]:
            new_city = City(name=city, region_id=value.id)
            new_city.save()
            print(new_city.name)
print("all cities are added")
