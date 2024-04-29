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
    cursor.execute('''CREATE TABLE IF NOT EXISTS entries (
                        date DATE,
                        id INTEGER PRIMARY KEY,
                        category TEXT,
                        name TEXT,
                        amount REAL
                    )''')
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Database created successfully at:", db_file)


def load_entries(current_date):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entries WHERE date = ?", (current_date,))
    entries = cursor.fetchall()
    conn.close()

    if entries:
        return entries

def total_amount():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(amount) FROM entries WHERE category = 'Income'")
    income = cursor.fetchone()[0]  # Fetch the sum of amounts

    cursor.execute("SELECT SUM(amount) FROM entries WHERE category = 'Expense'")
    expense = cursor.fetchone()[0]  # Fetch the sum of amounts

    total_balance = 0
    if income and expense:
        total_balance = income - expense
    elif income:
        total_balance += income

    conn.close()
    if total_balance:
        return total_balance



def add_data_to_table(date, category, name, amount):
    # Connect to SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    if category == "Expense":
        cursor.execute("INSERT INTO entries (date, category, name, amount) VALUES (?, ?, ?, ?)", (date, category, name, amount))
        conn.commit()

    if category == "Income":
        cursor.execute("INSERT INTO entries (date, category, name, amount) VALUES (?, ?, ?, ?)", (date, category, name, amount))
        conn.commit()
        
    # Close connection
    conn.close()
