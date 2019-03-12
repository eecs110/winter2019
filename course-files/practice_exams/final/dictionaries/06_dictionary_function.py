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
Problem 6:
Write a function called get_genre_artists that takes 
two positional parameters —  the artists dictionary 
as a genre (string) — and returns a list of artist 
names (list of strings) that match that genre.
'''

def get_genre_artists(data, genre):
    matching_names = []
    for key in artists:
        genres = data[key]['genres']
        if genre in genres:
            matching_names.append(key)
    return matching_names

# here's how I would invoke the function:
artist_names = get_genre_artists(artists, 'post-teen pop')

# and here's what would output if I printed it:
print('The post-teen pop artists are:', artist_names)