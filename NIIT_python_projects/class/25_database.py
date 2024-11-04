import sqlite3 as sql

connect = sql.connect('data/jumia.db')
cursor = connect.cursor()


query = """
DROP TABLE IF EXISTS orders
"""
cursor.execute(query)

query = """
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    qty REAL DEFAULT 1,
    date TEXT DEFAULT CURRENT_TIMESTAMP
)
"""
cursor.execute(query)


query = """
    INSERT INTO orders (product_id, unit_price, qty)
    VALUES (1, 150.0, 12),
    (2, 100.0, 12),
    (3, 500.0, 6),
    (4, 1400.0, 24),
    (5, 3500.0, 1.5)
"""
cursor.execute(query)


query = """
    SELECT * FROM orders
"""
cursor.execute(query)

result_set = cursor.fetchall()
print(result_set)


query = """
    SELECT * FROM products
"""
cursor.execute(query)

result_set = cursor.fetchall()
print(result_set)
