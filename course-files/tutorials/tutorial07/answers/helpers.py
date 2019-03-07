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

def extract_website_summary_from_webpage(soup):
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
    return summary.text
        
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
     # make unique:
    page_urls = list(set(page_urls))
    return page_urls
    return page_urls


def get_file_path(path, subdirectory=None):
    import sys
    import os
    dir_path = os.path.dirname(sys.argv[0])
    if subdirectory:
        return os.path.join(dir_path, subdirectory, path)
    else:
        return os.path.join(dir_path, path)


def write_pagerank_to_file(page_rank):
    # takes a dictionary as an argument
    pagerank_path = get_file_path('pagerank.txt', subdirectory='results')
    pagerank_file = open(pagerank_path, 'w')
    for key in sorted(page_rank, key=page_rank.get, reverse=True):
        pagerank_file.write(str(page_rank[key]) + ': ' + key + '\n')
    pagerank_file.close()
    
def write_links_to_file(urls):
    # takes a list of URLs as an argument
    logfile_path = get_file_path('links_to_crawl.txt', subdirectory='results')
    i = 1
    logger = open(logfile_path, 'w')
    for url in urls:
        logger.write(str(i) + ': ' + url + '\n')
        i += 1
    logger.close()
