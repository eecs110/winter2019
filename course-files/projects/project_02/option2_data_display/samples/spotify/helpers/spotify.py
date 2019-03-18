import urllib.request
from urllib.request import urlopen
import json

def get_token():
    # Handles security:
    url = 'https://eecs110-apis.herokuapp.com/spotify' # authenticates to Spotify
    results = urlopen(url).read().decode('utf-8', 'ignore')
    return json.loads(results)['token']

def _retrieve_from_spotify(url):
    request = urllib.request.Request(url, None, {
            'Authorization': 'Bearer ' + get_token()
        })
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode())
        return data

def get_tracks(search_term):
    search_term = urllib.parse.quote_plus(search_term)
    url = 'https://api.spotify.com/v1/search?q=' + search_term + '&type=track'
    return _retrieve_from_spotify(url)

def get_artists(search_term):
    search_term = urllib.parse.quote_plus(search_term)
    url = 'https://api.spotify.com/v1/search?q=' + search_term + '&type=artist'
    return _retrieve_from_spotify(url)

def get_track(track_id):
    url = 'https://api.spotify.com/v1/tracks/' + track_id
    return _retrieve_from_spotify(url)

def get_audio_features(track_id):
    url = 'https://api.spotify.com/v1/audio-features/' + track_id
    return _retrieve_from_spotify(url)

def get_audio_player_html(audio_url):
    return '''
    <audio id="audio" preload="auto" tabindex="0" controls="" type="audio/mp3">
        <source type="audio/mp3" src="{0}">Sorry, your browser does not support HTML5 audio.
    </audio>'''.format(audio_url)

def get_spotify_player(track_id):
    return '''
    <iframe src="https://open.spotify.com/embed?uri=spotify:track:{track_id}&amp;theme=white" width="300" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media" data-testid="audio-player">
    </iframe>
    '''.format(track_id=track_id)

def get_image_html(image_url):
    from IPython.display import Image
    return Image(url=image_url)._repr_html_()