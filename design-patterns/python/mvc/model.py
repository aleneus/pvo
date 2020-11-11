import sqlite3


class BuildingModel:
    def open_db(self, file_name):
        self.conn = sqlite3.connect(file_name)
        self.c = self.conn.cursor()

    def close_db(self):
        self.conn.close()

    def get_info(self):
        return list(self.c.execute("""
        SELECT * FROM rooms
        """))

    def get_purpose(self, number):
        return list(self.c.execute("""
        SELECT purpose FROM rooms WHERE number=?
        """, [number]))

    def get_numbers_by_purpose(self, purpose):
        return list(self.c.execute("""
        SELECT number FROM rooms WHERE purpose=?
        """, [purpose]))
