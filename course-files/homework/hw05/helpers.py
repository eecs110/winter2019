import sqlite3
import bs4
from urllib.request import urlopen

def get_webpage(url):
    try:
        # sleep 1 seconds to be polite
        results = urlopen(url).read().decode('utf-8', 'ignore')
        soup = bs4.BeautifulSoup(results, features='lxml')
        # remove unwanted tags (modifies soup object directly):
        [s.extract() for s in soup('script')]
        [s.extract() for s in soup('style')]
        return soup
    except:
        print('There was an error retrieving the following url:')
        print(url)
        return None

def get_words(text):
    import nltk
    import string
    nltk.download('stopwords')
    nltk.download('punkt')
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    
    excluded_words = set(
        stopwords.words('english') + list(string.punctuation)
    )
    words = word_tokenize(text)
    words_filtered = []
    
    # drop common and short words
    for w in words:
        if w not in excluded_words and len(w) > 3:
            words_filtered.append(w)
    words_filtered.sort()
    return words_filtered

    
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
    words = get_words(body.get_text().strip())
    return {
        'url': base_url,
        'title': title,
        'summary': summary.get_text().strip(),
        'words': ' '.join(words), # convert list to string
        'body': body.get_text().strip()
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


def create_or_replace_table():
    conn = sqlite3.connect(get_file_path('nu.db', subdirectory='results'))
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS Pages')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS "Pages" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
        "url" CHAR(2000),
        "title" CHAR(2000),
        "summary" TEXT,
        "body" TEXT,
        "words" TEXT,
        "page_rank" INTEGER)
    ''')
    cur.close()
    conn.close()

def insert_into_database(row):
    print('You are going to insert the extracted data into the database:', list(row.keys()))
    pass

def get_matching_pages(search_term):
    print('You are going to query the database to find all of the search results and then return them...')
    results = []
    return results
