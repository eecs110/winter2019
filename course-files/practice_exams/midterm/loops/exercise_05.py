def say_hello(name):
    print('Hello, ' + name + '! How are you today?')

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
    'David Blaine',
    'James Blake',
    'Corbin Bleu',
    'Orlando Bloom',
    'Jon Bon Jovi',
    'Asher Book',
    'David Boreanaz',
    'Tom Bott',
]

for name in names:
    if name[0] == 'J':
        say_hello(name)