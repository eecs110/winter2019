import helpers

some_data = [
    {'name': 'Sally', 'age': 34},
    {'name': 'Larry', 'age': 14},
    {'name': 'Vivian', 'age': 15},
    {'name': 'Mari', 'age': 20},
    {'name': 'Jessie', 'age': 50},
]
file_path = helpers.get_file_path('names.txt', subdirectory='results')
f = open(file_path, 'w')
for item in some_data:
    f.write(item['name'] + '\n')
f.close()
    