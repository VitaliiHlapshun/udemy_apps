import sqlite3

def connect():
    conn = sqlite3.connect("books_2.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS books_2 (id INTEGER PRIMARY KEY, text_title text, year integer, text_author text, isbn integer)")
    conn.commit()
    conn.close()


def insert(text_title, year, text_author, isbn):
    conn = sqlite3.connect("books_2.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books_2 (text_title,year,text_author,isbn) VALUES (?,?,?,?)",
                (text_title, year, text_author, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books_2.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books_2")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(text_title="", year="", text_author="", isbn=""):
    conn = sqlite3.connect("books_2.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books_2 WHERE text_title = ? OR year = ? OR text_author = ? OR isbn = ?",
                (text_title, year, text_author, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("books_2.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books_2 WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, text_title, year, text_author, isbn):
    conn = sqlite3.connect("books_2.db")
    cur = conn.cursor()
    cur.execute("UPDATE books_2 SET text_title = ?, year = ?, text_author = ?, isbn = ? WHERE id=?",
                (text_title, year, text_author, isbn, id))
    conn.commit()
    conn.close()



