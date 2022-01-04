import sqlite3

class Bookstore:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS books_2 (id INTEGER PRIMARY KEY, text_title text, year integer, text_author text, isbn integer)")
        self.conn.commit()

    def insert(self, text_title, year, text_author, isbn):
        self.cur.execute("INSERT INTO books_2 (text_title,year,text_author,isbn) VALUES (?,?,?,?)",
                    (text_title, year, text_author, isbn))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM books_2")
        rows = self.cur.fetchall()
        return rows


    def search(self, text_title="", year="", text_author="", isbn=""):
        self.cur.execute("SELECT * FROM books_2 WHERE text_title = ? OR year = ? OR text_author = ? OR isbn = ?",
                    (text_title, year, text_author, isbn))
        rows = self.cur.fetchall()
        self.conn.close()
        return rows


    def delete(self, id):
        self.cur.execute("DELETE FROM books_2 WHERE id=?", (id,))
        self.conn.commit()


    def update(self, id, text_title, year, text_author, isbn):
        self.cur.execute("UPDATE books_2 SET text_title = ?, year = ?, text_author = ?, isbn = ? WHERE id=?",
                    (text_title, year, text_author, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()