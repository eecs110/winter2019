import sqlite3
import helpers

conn = sqlite3.connect(helpers.get_file_path('../databases/flights.db'))
cur = conn.cursor()

# list columns for each of the available tables:
for table in ['airports', 'airlines', 'routes']:
    cur.execute("pragma table_info({0});".format(table))
    results = cur.fetchall()
    # add a little formatting to make things easier to read:
    print('\n')
    print(table)
    print('-' * 35)
    for row in results:
        print(row[1] + ' (' +  row[2] + ')')

cur.close()
conn.close()