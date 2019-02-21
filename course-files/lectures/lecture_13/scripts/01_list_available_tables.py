import sqlite3
import helpers

conn = sqlite3.connect(helpers.get_file_path('../databases/flights.db'))
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
# put the results of your query into the results variable:
results = cur.fetchall()
cur.close()
conn.close()

print(results)

# just adding a little formatting:
print()
print('List Tables:')
for row in results:
    print(row[0])

