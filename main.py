import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from datetime import datetime

class MoneyTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Money Tracker")

        # Initialize database
        self.conn = sqlite3.connect("finance.db")
        self.create_table()

        # Create UI elements
        self.create_widgets()
        self.load_entries()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS entries (
                            id INTEGER PRIMARY KEY,
                            date TEXT,
                            category TEXT,
                            amount REAL
                        )''')
        self.conn.commit()

    def create_widgets(self):
        # Treeview to display entries
        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("Date", "Category", "Amount")
        self.tree.heading("#0", text="ID")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Amount", text="Amount")
        self.tree.column("#0", width=50)
        self.tree.column("Date", width=100)
        self.tree.column("Category", width=100)
        self.tree.column("Amount", width=100)
        self.tree.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # Total label
        self.total_label = ttk.Label(self.root, text="Total: $0.00")
        self.total_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Button to add entry
        ttk.Button(self.root, text="+ Add Entry", command=self.add_entry_window).grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def load_entries(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM entries")
        rows = cursor.fetchall()

        total = 0
        for row in rows:
            amount = "${:.2f}".format(row[3])
            if row[2] == "Expense":
                total -= row[3]
                amount = "-" + amount  # Add '-' sign for expenses
                self.tree.insert("", "end", text=row[0], values=(row[1], row[2], amount), tags=("expense",))
            else:
                total += row[3]
                self.tree.insert("", "end", text=row[0], values=(row[1], row[2], amount), tags=("income",))
        self.total_label.config(text="Total: ${:.2f}".format(total))

        # Configure tag colors
        self.tree.tag_configure("income", foreground="green")
        self.tree.tag_configure("expense", foreground="red")

    def add_entry_window(self):
        self.add_window = tk.Toplevel(self.root)
        self.add_window.title("Add Entry")

        # Labels
        ttk.Label(self.add_window, text="Date:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.add_window, text="Category:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(self.add_window, text="Amount:").grid(row=2, column=0, padx=5, pady=5)

        # Entry fields
        self.date_entry = ttk.Entry(self.add_window)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)
        self.date_entry.insert(tk.END, datetime.now().strftime("%Y-%m-%d"))

        self.category_entry = ttk.Combobox(self.add_window, values=["Income", "Expense"])
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)
        self.category_entry.set("Expense")

        self.amount_entry = ttk.Entry(self.add_window)
        self.amount_entry.grid(row=2, column=1, padx=5, pady=5)

        # Button to add entry
        ttk.Button(self.add_window, text="Add", command=self.add_entry).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def add_entry(self):
        date = self.date_entry.get()
        category = self.category_entry.get()
        amount = self.amount_entry.get()

        if date and category and amount:
            try:
                amount = float(amount)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount")
                return

            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO entries (date, category, amount) VALUES (?, ?, ?)", (date, category, amount))
            self.conn.commit()

            self.tree.delete(*self.tree.get_children())
            self.load_entries()

            # Close add entry window
            self.add_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all fields")

def main():
    root = tk.Tk()
    app = MoneyTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
