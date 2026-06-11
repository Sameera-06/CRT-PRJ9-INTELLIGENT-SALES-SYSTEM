from database_connection import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales(
id INTEGER PRIMARY KEY AUTOINCREMENT,
date TEXT,
product TEXT,
sales INTEGER,
revenue REAL
)
""")

conn.commit()
conn.close()