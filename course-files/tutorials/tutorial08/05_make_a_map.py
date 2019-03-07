# https://python-visualization.github.io/folium/
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
    tiles="Stamen watercolor"   # Switch to "Stamen toner"
)

print('generating the map file...')
file_name = 'map_no_data.html'
file_path = helpers.get_file_path(file_name, subdirectory='results')
folium_map.save(file_path)