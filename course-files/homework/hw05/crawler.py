import time
import helpers


# each time you crawl, clear out your database and start over:
helpers.create_table_if_does_not_exist()
helpers.delete_all_rows_in_table()

# add the first link to crawl:  
urls = [
    'https://www.mccormick.northwestern.edu/eecs/courses/'
]
errors = {}
counter = 0
while len(urls) > 0:
    # get the next url
    url = urls.pop(0)
    soup = helpers.get_webpage(url)
    counter += 1
    if soup is None:
        errors['url'] = 1
        continue

    # extract urls from the web page
    webpage_urls = helpers.extract_links_from_webpage(soup, url)

    
    # extract key data from the web page:
    row = helpers.extract_data_from_webpage(soup, url)

    
    
    # Task 1: 
    # 1. Add the urls that you found to the urls list so that the
    #    webpage keeps crawling (b/c of the while loop condition)
    #    just like Tutorial 7.
    print('add webpage_urls to the urls list')
    #
    # 2. Insert a record of each page into the database: To do this, 
    #    update the insert_into_database so that it actually adds a new
    #    record to the "Pages" table. See 
    helpers.insert_into_database(row)

    # Don't forget to sleep for one second so we don't do a DDOS
    # attack on the Computer Science homepage!
    time.sleep(1)