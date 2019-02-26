import wikipedia
import bs4
import helpers

print('\nFetching page sections for wikipedia page...')
page = wikipedia.page('Northwestern_University')
headers = helpers.get_section_headers(page)

while True:
    # print menu:
    print()
    helpers.print_header('Menu: Northwestern University')
    counter = 1
    for header in headers:
        print(counter, header)
        counter += 1
    print()
    
    section_num = int(input('Which section do you want to read? '))
    header = headers[section_num - 1]
    section_text = helpers.get_section(page, header)

    # print user-selected section:
    print()
    helpers.print_header(header)
    print(section_text)
    input('\nPress enter to continue...')