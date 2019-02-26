import bs4

def get_section_headers(page):
    headers = []
    soup = bs4.BeautifulSoup(page.html(), features='lxml')
    result = soup.find('div', { 'id' : 'toc'})
    items = result.find_all('li')
    for li in items:
        line = li.text.strip().split('\n')[0]
        # remove numbers
        header = line.strip().split(' ')
        section_header = ' '.join(header[1:]).strip()
        if len(section_header) > 0:
            headers.append(section_header)
    return headers

def get_section(page, title):
    id = title.replace(' ', '_')
    paragraphs = []
    soup = bs4.BeautifulSoup(page.html(), features='lxml')
    try:
        result = soup.find('span', {'class': 'mw-headline', 'id': id})
        node = result.parent.nextSibling
        while node.name not in ['h2', 'h3']:
            if node.name:
                paragraphs.append(node.text.strip())
            node = node.nextSibling
        return '\n\n'.join(paragraphs)
    except:
        return 'No content could be found for "{0}" header'.format(title)

def print_header(header):
    print('-' * len(header))
    print(header.upper())
    print('-' * len(header))