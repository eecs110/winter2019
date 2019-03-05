data = {
    'results': [
        {
            'track': {
                'name': 'Crazy In Love',
                'duration': 400
            },
            'artist': {
                'name': 'Beyonce',
                'label': 'Columbia Records',
                'website': 'https://en.wikipedia.org/wiki/Beyonc%C3%A9'
            }
        },
        {
            'track': {
                'name': 'Love On Top',
                'duration': 287
            },
            'artist': {
                'name': 'Beyonce',
                'label': 'Columbia Records',
                'website': 'https://en.wikipedia.org/wiki/Beyonc%C3%A9'
            }
        }
    ],
    'total': 300,
    'page_num': 1
}

print(type(data))
print(data.keys())
results = data['results']
print(type(results))
first_result = results[0]
print(first_result)
print(type(first_result))
print(first_result.keys())
artist = first_result['artist']
print(artist)
print(type(artist))
print(artist.keys())
print(artist['name'])

'''
Question: what did we learn about this tree structure?
Answer:
    1. tracks is a dictionary
    2. The 'results' entry of the tracks dictionary is a list
    3. The first entry in the results list is a dictionary,
       which we stored, for convenience, in a variable called 
       "first_result."
    4. The first_result dictionary has an entry called "artist"
       (which is also a dictionary). We will store that dictionary
       in a variable called artist.
    5. The artist dictionary has an entry called "name", which stores
       the name of the artist. BINGO.
'''


# Now that we have learned about our data structure, 
# we can print all of the artist names to the screen:

print('*' * 18)
print('All artist names')
print('*' * 18)
results = data['results']
for track in results:
    print(track['artist']['name'])