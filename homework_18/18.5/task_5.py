import sqlite3


class DatabaseManager:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS table_name
                               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                column2 TEXT,
                                column3 TEXT)''')
        self.conn.commit()

    def insert_data(self):
        self.cursor.execute("INSERT INTO table_name (column2, column3) VALUES (?, ?)", ('data1', 'data2'))
        self.cursor.execute("INSERT INTO table_name (column2, column3) VALUES (?, ?)", ('data3', 'data4'))
        self.cursor.execute("INSERT INTO table_name (column2, column3) VALUES (?, ?)", ('data5', 'data6'))
        self.conn.commit()

    def delete_data(self):
        self.cursor.execute("DELETE FROM table_name WHERE id = ?", (2,))
        self.conn.commit()

    def update_data(self):
        self.cursor.execute("UPDATE table_name SET column2 = ?, column3 = ? WHERE id = ?", ('hello', 'world', 3))
        self.conn.commit()

    def export_to_file(self, file_name):
        self.cursor.execute("SELECT * FROM table_name")
        rows = self.cursor.fetchall()

        with open(file_name, 'w') as file:
            for row in rows:
                file.write(f"{row[0]}\t{row[1]}\t{row[2]}\n")


db_manager = DatabaseManager("database.db")
db_manager.create_table()
db_manager.insert_data()
db_manager.delete_data()
db_manager.update_data()
db_manager.export_to_file("data.txt")