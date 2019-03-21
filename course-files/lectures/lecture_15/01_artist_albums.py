# allows memory to import helpers from a sibling directory:
import helpers
from helpers import spotify
import pprint
import json
import os
import webbrowser

def write_to_file(data):
    file_path = helpers.get_file_path('spotify_artists.json', subdirectory='results')
    f = open(file_path, 'w')
    f.write(json.dumps(data))


search_term = input('Enter an artist or search term: ')
if search_term == '':
    search_term = 'Beyonce'
data = spotify.get_artists(search_term)

albums = spotify.get_albums(data['artists']['items'][0]['id'])

write_to_file(albums)


# Challenge: Figure out how to print the 
# name of the artist and the url to the artist's photo