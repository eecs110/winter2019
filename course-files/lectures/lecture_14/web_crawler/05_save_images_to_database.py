from urllib.request import urlopen
import bs4
import helpers
import time
import sqlite3

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

def create_table_if_does_not_exist(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    print('Creating an Images table (if it doesn\'t exist...')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS "Images" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
        "url" CHAR(2000))
    ''')
    cur.close()
    conn.close()

def delete_all_rows_in_table(db_path, table):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    print('Deleting all rows in', table, 'table...')
    cur.execute('DELETE FROM ' + table)
    cur.close()
    conn.commit()
    conn.close()

def save_urls_to_database(urls):
    db_path = helpers.get_file_path('test_database.db', subdirectory='results')
    create_table_if_does_not_exist(db_path)
    delete_all_rows_in_table(db_path, 'Images')

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    for url in urls:
        print('Writing', url, 'to the database...')
        cur.execute('''
            INSERT INTO Images (url)
            VALUES (?)''', 
            (url,)
        )
    cur.close()
    conn.commit()
    conn.close()


def get_webpage_html(url):
    return urlopen(url).read().decode('utf-8', 'ignore')




my_url = 'https://www.northwestern.edu/'
html = get_webpage_html(my_url)
urls = extract_images_from_webpage(html, my_url)

save_urls_to_database(urls)