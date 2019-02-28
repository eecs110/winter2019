# allows memory to import helpers from a sibling directory:
import helpers
from helpers import spotify
import pprint
import os
import webbrowser

search_term = input('Enter an artist or search term: ')
if search_term == '':
    search_term = 'Beyonce'
data = spotify.get_tracks(search_term)
# pprint.pprint(data)

def write_to_file(html):
    file_path = helpers.get_file_path('spotify_players.html', subdirectory='results')
    f = open(file_path, 'w')
    f.write(html)
    f.close()

    browser= webbrowser.get('chrome')
    absolute_path = os.path.abspath(file_path)
    browser.open('file://' + absolute_path)


elements = []
for track in data['tracks']['items']:
    track_id = track['id']
    # image element:
    elements.append(spotify.get_spotify_player(track_id))

write_to_file('''
    <html>
        <head><title>Songs</title></head>
        <body>
            <h1>{0}</h1>
            {1}
        </body>
'''.format(search_term, ''.join(elements)))