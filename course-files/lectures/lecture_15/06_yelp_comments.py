# Documentation: 
# * https://github.com/gfairchild/yelpapi
# * https://github.com/gfairchild/yelpapi/blob/master/examples/examples.py
# pip install yelpapi

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


# Challenge: Figure out how to print all of the reviews for Tomate on Noyes.