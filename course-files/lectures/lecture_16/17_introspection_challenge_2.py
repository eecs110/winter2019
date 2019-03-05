from helpers import spotify
import helpers
import pprint
import json


def write_to_file(results):
    file_path = helpers.get_file_path('spotify_tracks.json', subdirectory='results')
    f = open(file_path, 'w')
    f.write(json.dumps(results))
    f.close()


urls = []
search_term = 'Beyonce'
data = spotify.get_tracks(search_term)
write_to_file(data)
# pprint.pprint(data, depth=7)

'''
Challenge: using the same strategy as in file 14, how do
I print all of the album cover images? 
Hint: Here is what the data structure looks like:
https://codebeautify.org/jsonviewer/cbd57f4e

You can also view the results in the results/spotify_tracks.json file.
'''