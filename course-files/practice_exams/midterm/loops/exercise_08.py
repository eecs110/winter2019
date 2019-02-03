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

total_letters = 0
for name in names:
    total_letters += len(name)

print('The average number of letters is:', total_letters / len(names))