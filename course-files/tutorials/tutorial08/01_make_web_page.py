import helpers
import pprint
import json

artist = {
    "name": "Lady Gaga",
    "genres": ["dance pop", "pop"],
    "id": "1HY2Jd0NmPuamShAr6KMms",
    "image": {
        "height": 640,
        "url": "https://i.scdn.co/image/6fdeaf010a560e24ed9fdfab939dd0ab01d3d32c",
        "width": 640
    },
    "url": "https://api.spotify.com/v1/artists/1HY2Jd0NmPuamShAr6KMms"
}

template = '''
    <html>
        <head><title>{artist}</title></head>
        <body>
            <h1>{artist}</h1>
            <p>Genres: {genres}</p>
            <img src="{image_url}" />
        </body>
    </html>
'''

# Currently the template is being populated with the wrong
# data. Fix it so that it uses the data from artists:
html_text = template.format(
    artist='a',
    genres='b',
    image_url='c'
)

# write to file:
file_path = helpers.get_file_path('lady_gaga.html', subdirectory='results')
f = open(file_path, 'w')
f.write(html_text)
f.close()