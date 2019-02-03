names = [
    'Eugen Bauder',
    'William Beckett',
    'Tyson Beckford',
    'David Beckham',
    'Jason Behr',
    'Jonathan Bennett',
    'Sam Bennett',
    'Dierks Bentley',
    'Gael Garcia Bernal',
    'Jon Bernthal',
    'Wilson Bethel',
    'Justin Bieber',
    'Tom Bott',
    'David Blaine',
    'James Blake',
    'Corbin Bleu',
    'Orlando Bloom',
    'Jon Bon Jovi',
    'Asher Book',
    'David Boreanaz'
]

shortest_name = 'Z' * 1000  # initialize to a variable that guaranteed to be longer than any name in the list
for name in names:
    # print(name)
    if len(name) < len(shortest_name):
        print('old shortest name:', shortest_name)
        print('new shortest name:', name)
        shortest_name = name
print('*' * 50)
print('The shortest name is:', shortest_name)