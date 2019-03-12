artists = {
    'Lady Gaga': {
        'genres': ['dance pop', 'pop'],
        'image': {
            'url': 'https://i.scdn.co/image/6fdeaf010a560e24ed9fdfab939dd0ab01d3d32c',
            'width': 640
        },
    },
    'Rihanna': {
        'genres': ['dance pop', 'pop', 'post-teen pop', 'r&b', 'urban contemporary'],
        'image': {
            'url': 'https://i.scdn.co/image/1fc2f537d678d701d7d143a8fd4f0c2f29fbde22',
            'width': 640
        },
    },
    'Bob Dylan': {
        'genres': ['album rock', 'classic rock', 'folk'],
        'image': {
            'url': 'https://i.scdn.co/image/e8b81b4850f3374ecfc5c45eff323d17213dc6e4',
            'width': 1000
        },
    }
}

'''
Problem 5:
Write a function called get_image that takes two positional 
parameters — the artists dictionary as an artist name 
(string) — and returns the url of the image associated with 
the artist.
'''

def get_image_url(data, artist_name):
    return data[artist_name]['image']['url']

# here's how I would invoke the function:
image_url = get_image_url(artists, 'Rihanna')

# and here's what would output if I printed it:
print('The image url for Rihanna is:', image_url)