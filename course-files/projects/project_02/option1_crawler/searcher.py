import helpers
import webbrowser
import os

# 1. Prompt the user for a search term:
search_term = 'some term'

# 2. Implement the helpers.get_matching_pages function: 
results = helpers.get_matching_pages(search_term)

# loop through results and create an HTML link and paragraph
# for each entry. Append this text to the body_section variable:
body_section = ''
if len(results) == 0:
    body_section += '<p>No results found for {search_term}</p>'.format(search_term=search_term)
else:
    for page in results:
        # print(page)
        # 3. Build an HTML paragraph element where the url, title, and summary
        #    parameters come from the database. In other words, replace 
        #    'some url', 'some title', and 'some summary,' which are hard coded
        #    with actual results.

        body_section += '''
            <p>
                <a href="{url}">{title}</a><br>
                {summary}
            </p>
        '''.format(url='some url', title='some title', summary='some summary') 


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
absolute_path = os.path.abspath(file_path)

f = open(file_path, 'w')
f.write(template)
f.close()

print('Copy this link into your web browser to see the results:')
print('file://' + absolute_path)
try:
    # open web browser with the results:
    browser= webbrowser.get('chrome')
    browser.open('file://' + absolute_path)
except:
    print('Your web page did not open automatically.')

