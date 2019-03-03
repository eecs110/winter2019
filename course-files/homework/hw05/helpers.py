import sqlite3
import bs4
from urllib.request import urlopen

def get_webpage(url):
    try:
        # sleep 1 seconds to be polite
        results = urlopen(url).read().decode('utf-8', 'ignore')
        return bs4.BeautifulSoup(results, features='lxml')
    except:
        return None
    
def extract_data_from_webpage(soup, base_url):
    try:
        title = soup.find('title').text
    except:
        title = 'Untitled'
    body = soup.find('main')
    if body is None:
        try:
            body = soup.find('body')
        except:
            body = soup
    # get the first paragraph of the web page:
    summary = body.find('p')
    if not summary:
        summary = body

    return {
        'url': base_url,
        'title': title,
        'summary': summary.get_text(),
        'body': body.get_text()
    }


def get_base_url(base_url):
    return '/'.join(base_url.split('/')[0:-1]) + '/'


def get_root_url(base_url):
    return '/'.join(base_url.split('/')[0:3])


def stem_url(url):
    # gets rid of noise in the protocol to prevent duplicates:
    for prefix in ['http://', 'https://', 'https://www.', 'http://www.']:
        try:
            url = url.split(prefix)[1]
        except:
            pass
    return url


def has_been_visited(url, visited_dict):
    return visited_dict.get(stem_url(url)) is not None


def track_url(url, visited_dict):
    stemmed_url = stem_url(url) 
    if not visited_dict.get(stemmed_url):
        visited_dict[stemmed_url] = 0
    visited_dict[stemmed_url] += 1
    

def clean_url(url, base_url):
    # check if anchor tag:
    if url.startswith('#'):
        return None
        
    # remove query params and anchors:
    url = url.split('#')[0]
    url = url.split('?')[0]

    # if it starts with http, make sure it's a Northwestern website:
    if url.startswith('http'):
        if url.find('northwestern.edu') != -1:
            if not url.startswith('https'):
                url = url.replace('http', 'https')
            return url
        return None

    if url.startswith('/'):
        return get_root_url(base_url) + url
    else:
        base_url = get_base_url(base_url)
        while url.startswith('../'):
            url = ''.join(url.split('../'))
            base_url = '/'.join(base_url.split('/')[0:-2]) + '/'
        return base_url + url


def extract_links_from_webpage(soup, base_url):
    page_urls = []
    links = soup.find_all('a')
    for link in links:
        url = link.attrs.get('href')
        if url is not None:
            url = clean_url(url, base_url)
            if url is not None:
                page_urls.append(url)
    return page_urls


def get_file_path(path, subdirectory=None):
    import sys
    import os
    dir_path = os.path.dirname(sys.argv[0])
    if subdirectory:
        return os.path.join(dir_path, subdirectory, path)
    else:
        return os.path.join(dir_path, path)


def create_table_if_does_not_exist():
    conn = sqlite3.connect(get_file_path('nw.db'))
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS "Pages" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
        "url" CHAR(2000),
        "title" CHAR(2000),
        "summary" TEXT,
        "body" TEXT)
    ''')
    cur.close()
    conn.close()

def delete_all_rows_in_table():
    conn = sqlite3.connect(get_file_path('nw.db'))
    cur = conn.cursor()
    cur.execute('DELETE FROM Pages')
    cur.close()
    conn.commit()
    conn.close()

def insert_into_database(row):
    print('You are going to insert the extracted data into the database:', list(row.keys()))
    pass

def get_matching_pages(search_term):
    print('You are going to query the database to find all of the search terms...')
    pass
