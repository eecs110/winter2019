import helpers
import pprint
import json
import pandas as pd
pd.set_option('display.max_colwidth', -1) # so the table does not get truncated.

def display_image_html(entry):
    # instead of showing a dictionary, use the 'url' key to display an image:
    return '<img src="{0}" />'.format(entry['url'])

def display_genres(entry):
    # instead of showing a list, convert to a comma-separated string:
    return ', '.join(entry)

def display_link(entry):
    # instead of just showing the entry, convert the entry to a link:
    return '<a href="{0}">View on Spotify</a>'.format(entry)


file_path = helpers.get_file_path('artists.json', subdirectory='data_sources')
dataframe = pd.read_json(file_path)

# how we want each column to be displayed (see documentation):
# http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_html.html
formatters = {
    'image': display_image_html,
    'genres': display_genres,
    'url': display_link
}

template = '''
    <html>
        <head>
            <title>{header}</title>
            <link rel="stylesheet" href="styles.css" />
        </head>
        <body>
            <h1>{header}</h1>
            {table}
        </body>
    </html>
'''

html_text = template.format(
    header='A List of Spotify Artists',
    table=dataframe.to_html(
        justify='left', 
        escape=False, 
        columns=['name', 'genres', 'url', 'image'],
        formatters=formatters
    )
)

# write to file:
file_name = 'artists_table_formatted.html'
file_path = helpers.get_file_path(file_name, subdirectory='results')
f = open(file_path, 'w')
f.write(html_text)
f.close()