# https://python-visualization.github.io/folium/
'''
CHALLENGES:
1. Position the map so that it centers it on Northwestern’s campus.
2. Zoom in and out
3. Change the tiles: 
   https://python-graph-gallery.com/288-map-background-with-folium/
4. Using the documentation, can you figure out how to add a 
   marker to the map?
   https://python-visualization.github.io/folium/modules.html#module-folium.folium 
'''
import folium
import helpers


folium_map = folium.Map(
    location=[42.004583, -87.661406],
    zoom_start=13,
    tiles="Stamen toner"   # Switch to "Stamen watercolor" or "Stamen terrain"
)

print('generating the map file...')
file_name = 'map_no_data.html'
file_path = helpers.get_file_path(file_name, subdirectory='results')
folium_map.save(file_path)