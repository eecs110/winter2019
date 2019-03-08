import pandas as pd
import sqlite3
import helpers

# Now let's ask a different question. How many allegations are there
# by Beat?
file_path = helpers.get_file_path('cpd.db', subdirectory='data_sources')
conn = sqlite3.connect(file_path)
df = pd.read_sql_query('''
        SELECT beat_id, count(beat_id) as num_complaints
        FROM data_allegation
        GROUP BY beat_id 
        ORDER BY num_complaints desc;
    ''', conn)
pd.set_option('display.max_colwidth', -1) # so the table does not get truncated.

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

table_html = table=df.to_html(
    justify='left'
)
html_text = template.format(
    header='CPD Allegations',
    summary='Here, we can put a summary of this web page',
    table=table_html
)

file_path = helpers.get_file_path('table_cpd_by_beat.html', subdirectory='results')
f = open(file_path, 'w')
f.write(html_text)
f.close()

print('\n\nYour webpage has been generated here:\nfile://{0}\n\n'.format(file_path))