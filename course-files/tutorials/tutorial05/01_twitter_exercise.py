import urllib.request
import json
import pprint

# write a program that:
# 1. Prompts the user for a search term
# 2. Queries Twitter for status updates based on the search term
# 3. Iterates through the resulting data dictionary and
# 4. Prints the text of the status with the most retweets, 
#    along with the number of times the status has been retweeted.

url = 'https://eecs110-twitter-proxy.herokuapp.com/1.1/search/tweets.json?q='
url += 'northwestern'
request = urllib.request.urlopen(url)
data = json.loads(request.read().decode())
pprint.pprint(data, depth=3)