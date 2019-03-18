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

def write_to_file(results):
    file_path = helpers.get_file_path('yelp.json', subdirectory='results')
    f = open(file_path, 'w')
    f.write(json.dumps(results))
    f.close()

yelp_api = YelpAPI(get_yelp_key())
search_results = yelp_api.search_query(term='ice cream', location='evanston, IL', sort_by='rating', limit=5)
write_to_file(search_results)

businesses = search_results['businesses']
for business in businesses:
    print(business['name'])
    print(business['image_url'])
    print('\n')