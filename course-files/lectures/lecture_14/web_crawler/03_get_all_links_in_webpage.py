from urllib.request import urlopen
import bs4

def extract_links_from_webpage(html):
    soup = bs4.BeautifulSoup(html, features='lxml')
    urls = []
    link_tags = soup.find_all('a')
    for link_tag in link_tags:
        url = link_tag.attrs.get('href')
        if url is not None:
            urls.append(url)
    return urls

def get_webpage_html(url):
    return urlopen(url).read().decode('utf-8', 'ignore')

html = get_webpage_html('https://www.northwestern.edu')
links = extract_links_from_webpage(html)

for link in links:
    print(link)