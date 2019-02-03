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

longest_name = ''
for name in names:
    # print(name)
    if len(name) > len(longest_name):
        print('old longest name:', longest_name)
        print('new longest name:', name)
        longest_name = name
print('*' * 50)
print('The longest name is:', longest_name)