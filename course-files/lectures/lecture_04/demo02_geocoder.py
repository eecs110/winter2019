#############################################################################
# https://geocoder.readthedocs.io/
# Before running this code, install the geocoder module on command line: 
# 
# pip install geocoder
#
# Task 1: make a function called geocode() that take an address as a positional
# parameter and writes the results to a file.
#############################################################################
import geocoder
import json
import os
from time import sleep

address = 'Northwestern University, Evanston, IL, USA'
# sends a request over the web to geocode the address:
g = geocoder.osm(address)
# print(g.json)  # entire standardized address
print(g.latlng)

# output to a file:
dir_path = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(dir_path,"addresses.tsv")
my_file = open(file_name, "a")
print(address, g.latlng[0], g.latlng[1], sep='\t',
        file=my_file
    )

addresses = [
    'Mountain View, CA, USA',
    'Northwestern University, Evanston, IL, USA',
    'Chicago, IL, USA',
    'New York, USA'
]