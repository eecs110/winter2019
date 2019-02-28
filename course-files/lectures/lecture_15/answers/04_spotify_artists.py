# allows memory to import helpers from a sibling directory:
import helpers
from helpers import spotify
import pprint
import os
import webbrowser

def write_to_file(html):
    file_path = helpers.get_file_path('spotify_album_artists.html', subdirectory='results')
    f = open(file_path, 'w')
    f.write(html)
    f.close()
    browser= webbrowser.get('chrome')
    absolute_path = os.path.abspath(file_path)
    browser.open('file://' + absolute_path)


search_term = input('Enter an artist or search term: ')
if search_term == '':
    search_term = 'Beyonce'
data = spotify.get_artists(search_term)
# pprint.pprint(data, depth=4)

images = []
for artist in data['artists']['items']:
    name = artist['name']
    print(name)
    if len(artist['images']) > 1:
        thumb = artist['images'][1]['url']
        images.append(spotify.get_image_html(thumb))
    for image in  artist['images']:
        print(image['url'])
    

write_to_file('''
    <html>
        <head><title>Songs</title></head>
        <body>
            <h1>{0}</h1>
            {1}
        </body>
'''.format(search_term, ''.join(images)))