import sqlite3
import helpers

'''
Recall: airlines table:
index (INTEGER)
id (TEXT)
name (TEXT)
alias (TEXT)
iata (TEXT)
icao (TEXT)
callsign (TEXT)
country (TEXT)
active (TEXT)
'''

conn = sqlite3.connect(helpers.get_file_path('../databases/flights.db'))
cur = conn.cursor()
cur.execute(
    ''' UPDATE airlines
        SET id = ?, country = ?
        WHERE name = ?;
    ''', 
    (999, 'EECS110', 'EECS110')
)
conn.commit() # don't forget to save!


# Verify that it worked!
cur.execute("SELECT * FROM airlines WHERE id = 999;")
results = cur.fetchall()
cur.close()
conn.close()

for row in results:
    print(row)