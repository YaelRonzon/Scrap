import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

# customers_sql = """
# CREATE TABLE customers (
# first_name text,
#  last_name text)"""

# cur.execute(customers_sql)

sql_query = """INSERT INTO customers (first_name, last_name) VALUES ("Zeline", "Anersen")"""
cur.execute(sql_query)
conn.commit()

# cur.execute("SELECT first_name, last_name FROM customers")
# results = cur.fetchall()
# for row in results:
#     print(row)



sql = 'DELETE FROM customers WHERE last_name= "Anersen"'
cur.execute(sql)
conn.commit()

selected_query = """SELECT * FROM customers"""
cur.execute(selected_query)
rows = cur.fetchall()
for row in rows:
    print(row)


print("hi")