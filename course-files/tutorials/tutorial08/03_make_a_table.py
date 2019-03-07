import helpers
import pprint
import json
import pandas
pandas.set_option('display.max_colwidth', -1) # so the table does not get truncated.

file_path = helpers.get_file_path('artists.json', subdirectory='data_sources')
dataframe = pandas.read_json(file_path)


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
        columns=['name', 'genres', 'url', 'image']
    )
)

# write to file:
file_name = 'artists_table.html'
file_path = helpers.get_file_path(file_name, subdirectory='results')
f = open(file_path, 'w')
f.write(html_text)
f.close()