import pylab
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import helpers

# How do we display the same query as a bar chart?
# Answer: use pylab and matplotlib
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


# Instead of making a table, let's draw a barchart:
pylab.barh(
    beats, # beats on the y-axis
    counts, # count of allegations on the x-axis
    align="center", 
    alpha=0.5
)
# add chart labels:
pylab.xlabel('Num Complaints')
pylab.title('Number of Police Complaints by Beat')

# save image to the results directory
file_path = helpers.get_file_path('bar_chart_complaints.png', subdirectory='results')
plt.savefig(file_path)