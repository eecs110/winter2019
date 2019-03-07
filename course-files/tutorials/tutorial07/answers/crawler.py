import time
import helpers


# add the first link to crawl:  
urls = [
    'https://www.northwestern.edu/'
]
pagerank = {}
counter = 0
while len(urls) > 0:
    #########################
    # Don't forget to sleep #
    #########################
    time.sleep(2) 
    if counter > 20:
        break
    print(counter)
    counter += 1

    # removes the top url from the list
    url = urls.pop(0)
    print('\nretrieving ' + url + '...')
    soup = helpers.get_webpage(url)
    if soup is None:
        print('Error retrieving {url}'.format(url=url))
    else:
        website_summary = helpers.extract_website_summary_from_webpage(soup)
        links_on_page = helpers.extract_links_from_webpage(soup, url)

        for url in links_on_page:
            stemmed_url = helpers.stem_url(url)
            if pagerank.get(stemmed_url):
                pagerank[stemmed_url] += 1
            else:
                pagerank[stemmed_url] = 1

        urls += links_on_page

        print(website_summary)
        print(url)
        # print('*' * 80)
        # for key in sorted(pagerank, key=pagerank.get, reverse=True):
        #     print(pagerank[key], key)
        # print('*' * 80)
        # print()


helpers.write_links_to_file(urls)
helpers.write_pagerank_to_file(pagerank)