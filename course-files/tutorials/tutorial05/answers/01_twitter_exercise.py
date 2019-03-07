import urllib.request
import json
import pprint

# write a program that:
# 1. Prompts the user for a search term
# 2. Queries Twitter for status updates based on the search term
# 3. Iterates through the resulting data dictionary and
# 4. Prints the text of the status with the most retweets, 
#    along with the number of times the status has been retweeted.

search_term = input('Please enter a search term: ')
url = 'https://eecs110-twitter-proxy.herokuapp.com/1.1/search/tweets.json?q='
url += search_term
request = urllib.request.urlopen(url)
data = json.loads(request.read().decode())

# keep track of most re-Tweeted tweet:
most_retweeted = data['statuses'][0]
for status in data['statuses']:
    if most_retweeted['retweet_count'] < status['retweet_count']:
        most_retweeted = status

print('The most retweeted Tweet is:', most_retweeted['text'])
print('It has been retweeted', most_retweeted['retweet_count'], 'times.')