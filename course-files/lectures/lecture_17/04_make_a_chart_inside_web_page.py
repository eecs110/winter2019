import pylab
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import helpers

# get data:
file_path = helpers.get_file_path('cpd.db', subdirectory='data_sources')
conn = sqlite3.connect(file_path)
cur = conn.cursor()
cur.execute('''
    SELECT beat_id, count(beat_id) as num_complaints
    FROM data_allegation
    GROUP BY beat_id 
    ORDER BY num_complaints
    LIMIT 25;
''')
results = cur.fetchall()
cur.close()
conn.close()

# make a list with all of the beat names 
# and a list with all of the complaint counts
beats = []
counts = []
for result in results:
    # omit empty data:
    if result[0] is None or result[1] is None:
        continue
    beats.append('Beat ' + str(int(result[0])))
    counts.append(result[1])


# draw lots of lines on the same plot:
pylab.barh(
    beats, 
    counts, 
    align="center", 
    alpha=0.5
)
pylab.xlabel('Num Complaints')
pylab.title('Number of Police Complaints by Beat')

# save image to the results directory
chart_file_path = helpers.get_file_path('bar_chart_complaints', subdirectory='results')
plt.savefig(chart_file_path)



# ABOVE THIS LINE IS THE SAME AS 03_make_a_chart_group_by_sqlite
# But now, we're going to create a simple web page to display the
# chart:
template = '''
    <html>
        <head>
            <title>{header}</title>
            <link rel="stylesheet" href="styles.css" />
        </head>
        <body>
            <h1>{header}</h1>
            <p>{summary}</p>
            <img src="{chart_url}" />
        </body>
    </html>
'''
html_text = template.format(
    header='CPD Allegations',
    summary='Here, we can put a summary of this web page',
    chart_url=chart_file_path
)

html_file_path = helpers.get_file_path('chart_cpd.html', subdirectory='results')
f = open(html_file_path, 'w')
f.write(html_text)
f.close()