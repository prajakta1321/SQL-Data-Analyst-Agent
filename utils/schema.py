SCHEMA_INFO = """
Tables in the database:

customers:
- id (INTEGER, primary key)
- name (TEXT)
- email (TEXT)

products:
- id (INTEGER, primary key)
- name (TEXT)
- price (REAL)

orders:
- id (INTEGER, primary key)
- customer_id (INTEGER, foreign key → customers.id)
- product_id (INTEGER, foreign key → products.id)
- quantity (INTEGER)
- order_date (TEXT)
"""
