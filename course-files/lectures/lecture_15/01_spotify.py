from helpers import spotify
import pprint


urls = []
search_term = input('\nWhat artist do you want? ')
if search_term == '':
    search_term = 'Duran Duran'
data = spotify.get_tracks(search_term)

for item in data['tracks']['items']:
    urls.append(item['id'])
pprint.pprint(data, depth=4)

print(urls)
track = spotify.get_track(urls[0])
print(track['id'])

features = spotify.get_audio_features(track['id'])

for key in features:
    print(key, features[key], sep=': ')