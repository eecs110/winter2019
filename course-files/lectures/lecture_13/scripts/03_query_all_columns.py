import sqlite3
import helpers

conn = sqlite3.connect(helpers.get_file_path('../databases/flights.db'))
cur = conn.cursor()
cur.execute("SELECT * FROM airlines LIMIT 15;")
results = cur.fetchall()
cur.close()
conn.close()

for row in results:
    print(row)