import time
import helpers

# add the first link to crawl:  
url = 'https://www.northwestern.edu/'
print('retrieving ' + url + '...')
soup = helpers.get_webpage(url)
if soup is None:
    print('Error retrieving {url}'.format(url=url))
else:
    website_summary = helpers.extract_website_summary_from_webpage(soup)
    links_on_page = helpers.extract_links_from_webpage(soup, url)
    helpers.write_links_to_file(links_on_page)
    
    print(website_summary)
    for url in links_on_page:
        print(url)