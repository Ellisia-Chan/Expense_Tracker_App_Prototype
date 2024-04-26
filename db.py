import sqlite3
import os

# Get the directory where the py script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the SQLite database file
db_file = os.path.join(script_dir, "finance.db")

# Check if the database file already exists
if os.path.exists(db_file):
    print("Database already exists at:", db_file)
else:
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_file)

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create expenses table with date as the first column
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        date DATE,
                        id INTEGER PRIMARY KEY,
                        description TEXT,
                        amount REAL
                    )''')

    # Create income table with date as the first column
    cursor.execute('''CREATE TABLE IF NOT EXISTS income (
                        date DATE,
                        id INTEGER PRIMARY KEY,
                        source TEXT,
                        amount REAL
                    )''')

    # Create amount table
    cursor.execute('''CREATE TABLE IF NOT EXISTS amount (
                        id INTEGER PRIMARY KEY,
                        total_expenses REAL,
                        total_income REAL
                    )''')

    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Database created successfully at:", db_file)
