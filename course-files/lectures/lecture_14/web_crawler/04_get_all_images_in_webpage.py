from urllib.request import urlopen
import bs4
import helpers
import time

def extract_images_from_webpage(html, base_url):
    soup = bs4.BeautifulSoup(html, features='lxml')
    urls = []
    link_tags = soup.find_all('img')
    for link_tag in link_tags:
        url = link_tag.attrs.get('src')
        if url is not None:
            if not url.startswith('http'):
                url = base_url + url
            urls.append(url)
    return urls

def get_webpage_html(url):
    return urlopen(url).read().decode('utf-8', 'ignore')




my_url = 'https://www.northwestern.edu/'
html = get_webpage_html(my_url)
urls = extract_images_from_webpage(html, my_url)

for url in urls:
    # 1. get it from the internet
    results = urlopen(url).read()

    # 2. write it to a file
    file_name = url.split('/')[-1]
    print('writing {file_name} to the "results" directory...'.format(file_name=file_name))

    file_path = helpers.get_file_path(file_name, subdirectory='results')
    f = open(file_path, 'wb')
    f.write(results)
    f.close()
    time.sleep(2)