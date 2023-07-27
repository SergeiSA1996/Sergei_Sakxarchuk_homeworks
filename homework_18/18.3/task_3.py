import sqlite3
import random


conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS mytable
                  (id INTEGER PRIMARY KEY, field1 INTEGER, field2 INTEGER)''')

for i in range(5):
    field1 = random.randint(0, 9)
    field2 = random.randint(0, 9)
    cursor.execute("INSERT INTO mytable (field1, field2) VALUES (?, ?)", (field1, field2))
conn.commit()
cursor.execute("SELECT * FROM mytable ORDER BY RANDOM() LIMIT 1")
random_row = cursor.fetchone()


if random_row[1] % 2 == 0 and random_row[2] % 2 == 0:
    cursor.execute("DELETE FROM mytable WHERE id = ?", (random_row[0],))
else:
    cursor.execute("UPDATE mytable SET field1 = 2, field2 = 2 WHERE id = ?", (random_row[0],))

conn.commit()
cursor.execute("SELECT * FROM mytable")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()