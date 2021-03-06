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
    ''' INSERT INTO airlines(name, alias, iata, icao, callsign, country, active)
        VALUES(?, ?, ?, ?, ?, ?, ?)
    ''',
    ('EECS110', 'Intro to Computer Programming', '', '', '', 'USA', 'Y')
)
conn.commit() # don't forget to save!


# Verify that it worked!
cur.execute("SELECT * FROM airlines WHERE name = 'EECS110';")
results = cur.fetchall()
cur.close()
conn.close()

for row in results:
    print(row)