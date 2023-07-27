import sqlite3
import random


conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS mytable
                  (id INTEGER PRIMARY KEY, field1 INTEGER, field2 INTEGER)''')
for i in range(4):
    field1 = random.randint(0, 9)
    field2 = random.randint(0, 9)
    cursor.execute("INSERT INTO mytable (field1, field2) VALUES (?, ?)", (field1, field2))
conn.commit()
cursor.execute("SELECT AVG((field1 + field2) / 2) FROM mytable")
average = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM mytable")
count = cursor.fetchone()[0]
if average > count:
    cursor.execute("SELECT id FROM mytable LIMIT 1 OFFSET 3")
    row_id = cursor.fetchone()[0]
    cursor.execute("DELETE FROM mytable WHERE id = ?", (row_id,))
conn.commit()
cursor.execute("SELECT * FROM mytable")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()