# https://blog.prototypr.io/interactive-maps-with-python-part-1-aa1563dbe5a9
# https://nbviewer.jupyter.org/github/vincentropy/python_cartography_tutorial/blob/master/part1_basic_folium_maps.ipynb
import folium
import json
import urllib
import helpers
import pprint


folium_map = folium.Map(
    location=[42.004583, -87.661406],
    zoom_start=13,
    tiles="Stamen toner"   # Switch to "Stamen watercolor"
)

# add some markers to the map...
print('retrieving bike station data...')
request = urllib.request.urlopen('https://feeds.divvybikes.com/stations/stations.json')
data = json.loads(request.read().decode())
# pprint.pprint(data)

print('creating map markers...')
for station in data['stationBeanList']:
    name = station['stationName']
    lat = station['latitude']
    lng = station['longitude']
    available_bikes = station['availableBikes']
    # print(name, lat, lng, available_bikes)

    marker = folium.CircleMarker(
        location=[lat, lng],
        color='teal', 
        radius=available_bikes * 8,
        fill_color='teal',
        fill_opacity=0.6)
    marker.add_to(folium_map)


print('generating the map file...')
file_name = 'divvy_bike_map.html'
file_path = helpers.get_file_path(file_name, subdirectory='results')
folium_map.save(file_path)