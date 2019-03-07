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
    tiles="Stamen watercolor"   # Try other options! Stamen toner
)

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

template = '''
    <html>
        <head>
            <title>{header}</title>
            <link rel="stylesheet" href="styles.css" />
        </head>
        <body>
            <h1>{header}</h1>
            <p>{summary}</p>
            <div style="width: 800px; margin:auto;">
                {map}
            </div>
        </body>
    </html>
'''
html_text = template.format(
    header='My Webpage Title',
    summary='Here, we can put a summary of this web page',
    map=folium_map._repr_html_()
)

print('generating the map file...')
file_path = helpers.get_file_path('embedded_map.html', subdirectory='results')
f = open(file_path, 'w')
f.write(html_text)
f.close()