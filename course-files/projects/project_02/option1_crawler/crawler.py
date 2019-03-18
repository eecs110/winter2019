import time
import helpers


# each time you crawl, clear out your database and start over:
helpers.create_or_replace_table()

# add the first link to crawl:  
urls = [
    'https://www.mccormick.northwestern.edu/eecs/'
]
visited = {}
counter = 0
while len(urls) > 0:
    # get the next url
    url = urls.pop(0)
    soup = helpers.get_webpage(url)
    counter += 1

    # extract urls from the web page (already done for you)
    webpage_urls = helpers.extract_links_from_webpage(soup, url)
    
    # extract key data from the web page (already done for you):
    # (print the row variable to understand it)
    row = helpers.extract_data_from_webpage(soup, url)
    print(row['body'])
    urls += webpage_urls

    
    # YOUR TASKS:
    # 1. Add the urls that you found to the urls list so that the
    #    webpage keeps crawling (b/c of the while loop condition)
    #    just like Tutorial 7.
    print('add webpage_urls to the urls list')

    # 2. Track how many times each url has been visited as you crawl; 
    #    and don't crawl the same page twice.

    # 3. Insert a record of each page into the database: To do this, 
    #    update the helpers.insert_into_database function so that it 
    #    actually adds a new record to the "Pages" table. 
    #    See Python Notebooks from Lecture 13 for samples:
    #    lecture_13/notebooks/02_creating_updating_deleting_data.ipynb
    helpers.insert_into_database(row)


    # Don't forget to sleep for one second so we don't do a DDOS
    # attack on the Computer Science homepage!
    time.sleep(1)

# 4. After the loop has exited, print your dictionary of links visited
#    and the counts below: