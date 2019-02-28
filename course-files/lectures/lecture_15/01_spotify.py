from helpers import spotify
import helpers
import pprint
import json


def write_to_file(results):
    file_path = helpers.get_file_path('spotify_artists.json', subdirectory='results')
    f = open(file_path, 'w')
    f.write(json.dumps(results))
    f.close()


urls = []
search_term = input('\nSearch songs for which artist? ')
if search_term == '':
    search_term = 'Beyonce'
data = spotify.get_tracks(search_term)

for item in data['tracks']['items']:
    urls.append(item['id'])
write_to_file(data)
pprint.pprint(data, depth=4)

print(urls)
track = spotify.get_track(urls[0])
print(track['id'])

features = spotify.get_audio_features(track['id'])

for key in features:
    print(key, features[key], sep=': ')