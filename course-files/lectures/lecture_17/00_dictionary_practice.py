import helpers
import pprint
import json

file_path = helpers.get_file_path('artists.json', subdirectory='data_sources')
f = open(file_path, 'r')
artists = json.load(f)
# pprint.pprint(artists)

print(artists)


'''
Challenges: 
1. Print the name of the third artist in the list
2. Print the url that is associated with the image for the second artist
3. Build a list of image urls
4. Print the name of all of the artists
'''