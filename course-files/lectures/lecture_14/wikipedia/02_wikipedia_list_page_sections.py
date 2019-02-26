import wikipedia
import bs4
import helpers

print('\nFetching page sections for wikipedia page...')
page = wikipedia.page('Northwestern_University')
headers = helpers.get_section_headers(page)

counter = 1
for header in headers:
    print(counter, header)
    counter += 1