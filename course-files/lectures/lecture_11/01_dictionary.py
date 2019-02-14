#example: 
eng2sp = {
    'one': 'uno', 
    'two': 'dos', 
    'three': 'tres'
}
print(eng2sp)
print(eng2sp.keys())
print(eng2sp.values())
print(eng2sp['three'])
print(eng2sp.get('three'))
print(eng2sp.get('four'))   # use to check to see if an entry exists in the dictionary
# print(eng2sp['four'])     # this will throw a KeyError exception
