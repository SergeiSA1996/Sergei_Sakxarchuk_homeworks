import sqlite3


class DatabaseManager:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def manipulate_db(self, *args):
        if len(args) == 1:
            self.cursor.execute("INSERT INTO table_name (column_name) VALUES (?)", (3,))
        elif len(args) == 2:
            if isinstance(args[1], int):
                self.cursor.execute("DELETE FROM table_name LIMIT 1")
            elif isinstance(args[0], int) and isinstance(args[1], int) and isinstance(args[2], int):
                self.cursor.execute("UPDATE table_name SET column_name = ? WHERE id = ?", (77, 3))

        self.conn.commit()


db_manager = DatabaseManager("database.db")
db_manager.manipulate_db(1)
db_manager.manipulate_db(2, 5)
db_manager.manipulate_db(1, 2, 3)
