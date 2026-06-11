import sqlite3

def get_connection():
    conn = sqlite3.connect("database/sales.db")
    return conn