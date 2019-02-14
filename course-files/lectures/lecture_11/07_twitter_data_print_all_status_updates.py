import urllib.request
import json
import pprint  # module that makes it easier to print and look at dictionaries

# Challenge: write a program that prints all of the status updates

search_term = input('Please enter a search term (defaults to "northwestern"): ')
if search_term == '':
    search_term = 'Northwestern'
url = 'https://eecs110-twitter-proxy.herokuapp.com/1.1/search/tweets.json?q='
url += search_term
request = urllib.request.urlopen(url)
data = json.loads(request.read().decode())

pprint.pprint(data, depth=1)