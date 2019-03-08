import pandas
import sqlite3
import helpers

# The goal of this program is to create an HTML page with a 
# table of CPD allegations:

# 1. Get data from the database:
file_path = helpers.get_file_path('cpd.db', subdirectory='data_sources')
conn = sqlite3.connect(file_path)
df = pandas.read_sql_query('''
        SELECT * 
        FROM data_allegation
        WHERE length(summary) > 20 
        ORDER BY incident_date desc
        LIMIT 50;
    ''', conn)
pandas.set_option('display.max_colwidth', -1) # so the table does not get truncated.

# 2. Create a simple HTML Template:
template = '''
    <html>
        <head>
            <title>{header}</title>
            <link rel="stylesheet" href="styles.css" />
        </head>
        <body>
            <h1>{header}</h1>
            <p>{summary}</p>
            {table}
        </body>
    </html>
'''

# Ask Pandas to create an HTML representation of the table,
# but only for the columns specified in the columns argument:
table_html = table=df.to_html(
    justify='left',
    columns=['id', 'incident_date', 'summary', 'beat_id']
)

# Merge the data with the template using the string format function:
html_text = template.format(
    header='CPD Allegations',
    summary='Here, we can put a summary of this web page',
    table=table_html
)

# write the final HTML page to a file:
file_path = helpers.get_file_path('table_cpd.html', subdirectory='results')
f = open(file_path, 'w')
f.write(html_text)
f.close()

print('\n\nYour webpage has been generated here:\nfile://{0}\n\n'.format(file_path))