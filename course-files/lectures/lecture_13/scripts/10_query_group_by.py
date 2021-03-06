import sqlite3
import helpers

conn = sqlite3.connect(helpers.get_file_path('../databases/flights.db'))
cur = conn.cursor()
cur.execute('''
   SELECT country, count(country) as airline_count
    FROM airlines
    GROUP BY country
    ORDER BY airline_count desc
    LIMIT 25;
''')
results = cur.fetchall()
cur.close()
conn.close()

for row in results:
    print(row)