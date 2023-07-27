import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS mytable
                  (text1 TEXT, text2 TEXT, number INTEGER)''')
number = int(input("Введите число: "))

text1 = "Привет"
text2 = "Мир"
cursor.execute("INSERT INTO mytable VALUES (?, ?, ?)", (text1, text2, number))
conn.commit()
cursor.execute("SELECT * FROM mytable")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()