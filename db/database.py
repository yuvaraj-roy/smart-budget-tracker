import sqlite3
import os

DB_PATH = os.path.join("data","expenses.db")

def get_connection():
    """Return a connection object to the SQLite database."""
    return sqlite3.connect(DB_PATH)

def initialize_db():
    """Create expenses table if it doesn't exist"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL
        )    
    ''')

    conn.commit()
    conn.close()