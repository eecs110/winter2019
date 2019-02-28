import time
import helpers

# add the first link to crawl:  
url = 'https://www.northwestern.edu/'
print('retrieving ' + url + '...')
soup = helpers.get_webpage(url)
if soup is None:
    print('Error retrieving {url}'.format(url=url))
else:
    website_summary = helpers.get_website_summary(soup)
    links_on_page = helpers.extract_links_from_webpage(soup, url)
    helpers.log_links_to_crawl_to_file(links_on_page)
    
    print(website_summary)
    for url in links_on_page:
        print(url)