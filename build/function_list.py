from pathlib import Path
from tkinter import ttk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
import tkinter as tk

# Function to create a new window
def add_button(window):
    new_window = Toplevel(window)
    new_window.title("Add Items")
    new_window.geometry("400x300")
    new_window.config(bg="#102C57")

    # Frames
    frame = ttk.Frame(new_window, style="New.TFrame", width=340, height=230)

    frame.place(x=30, y=30)

    # Lbl
    ttk.Label(frame, text="Category:", font=("katibeh", 16, "bold"), background="#EADBC8").place(x=10, y=20)
    ttk.Label(frame, text="Name:", font=("katibeh", 16, "bold"), background="#EADBC8").place(x=10, y=60)
    ttk.Label(frame, text="Amount:", font=("katibeh", 16, "bold"), background="#EADBC8").place(x=10, y=100)

    # Category ComboBox
    ent_category = ttk.Combobox(frame, values=["Income", "Expense"], font=("katibeh", 16), width=12)

    ent_category.set("Expense")

    # Entry
    ent_name = ttk.Entry(frame, font=("katibeh", 16), width=16)

    ent_amount = ttk.Entry( frame, font=("katibeh", 16), width=14)

    ent_category.place(x=130, y=20)
    ent_name.place(x=90, y=60)
    ent_amount.place(x=110, y=100)

    # Add Button
    btn_add = tk.Button(frame, text="Add", font=("katibeh", 16), width=9, command=self.add_to_db)
    
    btn_add.place(x=110, y=170)
    
    