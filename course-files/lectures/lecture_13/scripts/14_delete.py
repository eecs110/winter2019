import sqlite3
import helpers

conn = sqlite3.connect(helpers.get_file_path('../databases/flights.db'))
cur = conn.cursor()
cur.execute(
    'DELETE from airlines WHERE id = ?;',
    (999,)
)
conn.commit() # don't forget to save!


# Verify that it worked!
cur.execute('SELECT * FROM airlines WHERE id = ?;', (999,))
results = cur.fetchall()
cur.close()
conn.close()

print(results)