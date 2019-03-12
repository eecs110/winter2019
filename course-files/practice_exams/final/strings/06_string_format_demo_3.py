import helpers

template = '{0} is {1} years old.'

some_data = [
    {'name': 'Sally', 'age': 34},
    {'name': 'Larry', 'age': 14},
    {'name': 'Vivian', 'age': 15},
    {'name': 'Mari', 'age': 20},
    {'name': 'Jessie', 'age': 50},
]

for item in some_data:
    print(template.format(*item.values()))