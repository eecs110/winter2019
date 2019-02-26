import wikipedia
import bs4
import helpers
import time



term = input('\nWhat do you want to search for? ')
results = wikipedia.search(term)

print('\nI found the following items for you. What would you like to do?\n')

for i, item in enumerate(results):
    print((i+1), item, sep='. ')

option = int(input('\nWhat do you want to do? '))
search_term = results[option - 1]
print('Retrieving', search_term, 'page...')
page = wikipedia.page(search_term)
headers = helpers.get_section_headers(page)

while True:
    helpers.print_header(search_term + ' Menu')
    print('1. Summary')
    for i, header in enumerate(headers):
        print((i+2), header, sep='. ')

    option = int(input('\nWhich section? ')) - 2
    if option == -1:
        helpers.print_header('Summary')
        print(page.summary)
    else:
        # get section:
        header = headers[option]
        text = helpers.get_section(page, header)

        # print section:
        helpers.print_header(header)
        print(text)
    input('\nPress enter to continue...')
