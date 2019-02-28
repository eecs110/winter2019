import time
import helpers


# add the first link to crawl:  
urls = [
    'https://www.northwestern.edu/'
]
pagerank = {}
while len(urls) > 0:
    #########################
    # Don't forget to sleep #
    #########################
    time.sleep(2) 

    # removes the top url from the list
    url = urls.pop(0)
    print('\nretrieving ' + url + '...')
    soup = helpers.get_webpage(url)
    if soup is None:
        print('Error retrieving {url}'.format(url=url))
    else:
        website_summary = helpers.get_website_summary(soup)
        links_on_page = helpers.extract_links_from_webpage(soup, url)
        helpers.log_links_to_crawl_to_file(links_on_page)
        
        print(website_summary)
        
        # Goal: modify this code to crawl through all the links of the northwestern
        # website, and track how many times each website is linked to, using a dictionary.

    