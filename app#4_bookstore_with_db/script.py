import psycopg2


def create_db():
    conn = psycopg2.connect("dbname='udemy_db' user='odoo13' password='odoo13' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert_data(item, quantity, price):
    conn = psycopg2.connect("dbname='udemy_db' user='odoo13' password='odoo13' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='udemy_db' user='odoo13' password='odoo13' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete():
    conn = psycopg2.connect("dbname='udemy_db' user='odoo13' password='odoo13' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store")
    conn.commit()
    conn.close()

create_db()
# insert_data("Apple", 10, 20.5)
print(view())
delete()