# Documentation: https://github.com/gfairchild/yelpapi/blob/master/examples/examples.py
from yelpapi import YelpAPI
from urllib.request import urlopen
import helpers
import json

def get_yelp_key():
    # Handles security:
    url = 'https://eecs110-apis.herokuapp.com/yelp' # gets Yelp Token
    results = urlopen(url).read().decode('utf-8', 'ignore')
    return json.loads(results)['token']

def write_to_file(results, file_name='yelp_data.json'):
    file_path = helpers.get_file_path(file_name, subdirectory='results')
    f = open(file_path, 'w')
    f.write(json.dumps(results))
    f.close()


def get_yelp_categories_children(parent):
    f = open(helpers.get_file_path('categories.json'), 'rb')
    data = json.loads(f.read()) 
    categories = []
    for record in data:
        if parent in record['parents']:
            categories.append(record['title'])
    categories.sort()
    return categories

def get_restaurant_categories():
    return get_yelp_categories_children('restaurants')

def make_menu():
    bar = '-' * 40
    print()
    print(bar)
    print('Main Menu')
    print(bar)
    print('1. View cuisine choices')
    print('2. Find restaurant')
    print('3. Get restaurant details (as HTML)')
    print('4. Get restaurant reviews (as HTML)')
    print('5. Quit')
    print(bar)
    print()

def print_categories():
    categories = get_restaurant_categories()
    counter = 1
    for category in categories:
        print('{num}. {category}'.format(num=counter, category=category))
        counter += 1

# Challenge: Figure out how to print all of the reviews for Tomate on Noyes.


while True:
    make_menu()
    choice = input('What would you like to do? ')
    if choice == '1':
        print_categories()
    elif choice == '2':
        yelp_api = YelpAPI(get_yelp_key())
        # kind_of_food = input('what do you want to eat?')
        search_results = yelp_api.search_query(
            term='Pizza', 
            location='Evanston, IL', 
            sort_by='rating', 
            limit=25
        )    
        write_to_file(search_results, 'yelp_pizza.json')
        businesses = search_results['businesses']
        counter = 1
        for business in businesses:
            print('{num}. {business}'.format(num=counter, business=business['name']))
            counter += 1
    
    elif choice == '3':
        print('get restaurant detail...')
    
    elif choice == '4':
        print('get restaurant reviews...')
    
    elif choice == '5':
        print('Goodbye!')
        break
    
    input('\nPress any key to continue...')
