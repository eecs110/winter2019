import helpers
import pprint
import json

file_path = helpers.get_file_path('artists.json', subdirectory='data_sources')
f = open(file_path, 'r')
artists = json.load(f)
pprint.pprint(artists)

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

html_text = template.format(
    artist='a',
    genres='b',
    image_url='c'
)

# write to file:
file_name = 'artist.html'
file_path = helpers.get_file_path(file_name, subdirectory='results')
f = open(file_path, 'w')
f.write(html_text)
f.close()