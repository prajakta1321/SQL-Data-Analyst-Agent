import sqlite3

def create_db():
    conn = sqlite3.connect("db/sales.db")
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        city TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        price REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        FOREIGN KEY(customer_id) REFERENCES customers(id),
        FOREIGN KEY(product_id) REFERENCES products(id)
    )
    """)

    # Insert sample data
    cursor.executemany(
        "INSERT INTO customers (name, city) VALUES (?, ?)",
        [
            ("Amit", "Mumbai"),
            ("Neha", "Pune"),
            ("Rahul", "Delhi")
        ]
    )

    cursor.executemany(
        "INSERT INTO products (product_name, price) VALUES (?, ?)",
        [
            ("Laptop", 55000),
            ("Phone", 20000),
            ("Headphones", 3000)
        ]
    )

    cursor.executemany(
        "INSERT INTO orders (customer_id, product_id, quantity) VALUES (?, ?, ?)",
        [
            (1, 1, 1),
            (2, 2, 2),
            (3, 3, 3)
        ]
    )

    conn.commit()
    conn.close()
    print("sales.db created with sample data")

if __name__ == "__main__":
    create_db()

