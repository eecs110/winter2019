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

def get_artist_names(data):
    return list(data.keys())

# invoke function:
names = get_artist_names(artists)

# let's print it out to see what we have:
print(type(names))
print(names)
for name in names:
    print(name)