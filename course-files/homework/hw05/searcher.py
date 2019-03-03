import helpers
import webbrowser
import os

search_term = input('enter search term: ')
results = helpers.get_matching_pages(search_term)

# loop through results and create an HTML link and paragraph
# for each entry. Append this text to the body_section variable:
body_section = ''
if len(results) == 0:
    body_section += '<p>No results found for {search_term}</p>'.format(search_term=search_term)
else:
    for r in results:
        body_section += '''
            <p>
                <a href="{url}">{title}</a><br>
                {summary}
            </p>
        '''.format(url=r[1], title=r[2], summary=r[3]) 


# inject results into simple HTML page:
template = '''
    <html>
        <head>
            <title>Northwestern Search Results</title>
        </head>
        <body>
            <h1>Search Results</h1>
            {body}
        </body>
    </html>
'''.format(body=body_section)

# write everything to a file:
file_path = helpers.get_file_path(search_term.replace(' ', '_') + '.html', subdirectory='results')
# file_path = os.path.join('results', file_path)
print(file_path)
f = open(file_path, 'w')
f.write(template)
f.close()

# open web browser with the results:
browser= webbrowser.get('chrome')
absolute_path = os.path.abspath(file_path)
browser.open('file://' + absolute_path)

