import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import db


class StartUp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x200")
        self.overrideredirect(True)

        # Center StartUp Window
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry("+{}+{}".format(x, y))

        # Call methods
        self.create_widgets()
        self.loading(0)

    def create_widgets(self):
        # Frame
        self.frame = tk.Frame(self, width=500, height=200, bd=10, relief=tk.GROOVE, bg="#102C57")
        self.frame.pack()

        # Lbl
        lbl_title = tk.Label(self.frame, text="Pera Ko", font=("kuashan script", 40, "bold"), bg="#102C57", fg="#fff")
        lbl_title.place(x=150, y=50)
        self.lbl_loading = tk.Label(self.frame, text="0 %", font=("kuashan script", 18, "bold"), bg="#102C57",
                                    fg="#fff")
        self.lbl_loading.place(x=230, y=120)

    def loading(self, progress):
        if progress <= 100:
            self.lbl_loading.config(text=f"{progress} %")
            progress += 1
            self.after(10, self.loading, progress)
        else:
            self.destroy()
            window = MyApp()
            window.mainloop()


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x750")
        self.title("Pera ko")
        self.resizable(False, False)

        self.create_widgets()
        self.load_entries()
        self.update_total_balance()

    def create_widgets(self):
        # Frames
        self.top_frame = tk.Frame(self, width=500, height=180, bg="#102C57")
        self.mid_frame = tk.Frame(self, width=500, height=490, bg="#EADBC8")
        self.bot_frame = tk.Frame(self, width=500, height=80, bg="#102C57")

        # Frames pos
        self.top_frame.place(x=0, y=0)
        self.mid_frame.place(x=0, y=180)
        self.bot_frame.place(x=0, y=670)

        # Date
        self.current_date = tk.StringVar()
        self.current_date.set(datetime.now().strftime("%B %d, %Y"))

        self.lbl_date = tk.Label(self.top_frame, textvariable=self.current_date, font=("katibeh", 20, "bold"),
                                 bg="#102C57", fg="#fff")
        lbl_expenses = tk.Label(self.top_frame, text="Expenses", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff")
        lbl_income = tk.Label(self.top_frame, text="Income", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff")
        lbl_balance = tk.Label(self.top_frame, text="Balance", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff")

        self.lbl_expenses_amount = tk.Label(self.top_frame, text="₱0", font=("katibeh", 14, "bold"),
                                            bg="#102C57", fg="#FF0000")
        self.lbl_income_amount = tk.Label(self.top_frame, text="₱0", font=("katibeh", 14, "bold"),
                                           bg="#102C57", fg="#90EE90")
        self.lbl_amount_amount = tk.Label(self.top_frame, text="₱0", font=("katibeh", 14, "bold"),
                                           bg="#102C57", fg="#fff")

        btn_menu = tk.Button(self.top_frame, text="≡", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff", width=3)
        btn_search = tk.Button(self.top_frame, text="🔍", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff", width=3)

        self.btn_date_next = tk.Button(self.top_frame, text=">", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff",
                                  width=3, command=self.next_date)
        self.btn_date_previous = tk.Button(self.top_frame, text="<", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff",
                                      width=3, command=self.previous_date)

        # Top Frame Widgets pos
        self.lbl_date.place(x=160, y=50)
        lbl_expenses.place(x=40, y=110)
        lbl_income.place(x=210, y=110)
        lbl_balance.place(x=360, y=110)

        self.lbl_expenses_amount.place(x=30, y=140)
        self.lbl_income_amount.place(x=200, y=140)
        self.lbl_amount_amount.place(x=350, y=140)

        btn_menu.place(x=10, y=10)
        btn_search.place(x=450, y=10)

        self.btn_date_next.place(x=360, y=50)
        self.btn_date_previous.place(x=100, y=50)

        # Mid Frame widgets
        self.tv_tree_view = ttk.Treeview(self.mid_frame, columns=(1, 2, 3), show="headings", height=23, style="Custom.Treeview")
        self.tv_tree_view.column(1, anchor="center", stretch="No", width=80)
        self.tv_tree_view.column(2, anchor="center", stretch="No", width=200)
        self.tv_tree_view.column(3, anchor="center", stretch="No", width=200)
        self.tv_tree_view.heading(1, text="ID")
        self.tv_tree_view.heading(2, text="Name")
        self.tv_tree_view.heading(3, text="Amount")

        self.tv_tree_view.pack(side="left")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview.Heading", font=("katibeh", 18))
        style.configure("Custom.Treeview", font=("katibeh", 16), background="#EADBC8", fieldbackground="#EADBC8")
        style.configure("Custom.Treeview", rowheight=30)

        self.tv_tree_view.bind('<Button-1>', 'break')

        scrollbar = ttk.Scrollbar(self.mid_frame, orient="vertical", command=self.tv_tree_view.yview)
        scrollbar.pack(side="right", fill="y")

        # Btn
        btn_edit = tk.Button(self.mid_frame, text="✍", font=("katibeh", 24))
        btn_edit.place(x=400, y=400)

        # Bot Frame
        btn_add = tk.Button(self.bot_frame, text="+", font=("katibeh", 30), bg="#FEFAF6", command=self.add_entry_win)
        btn_add.place(x=220, y=0)
        
        # Enable Disable Widgets
        # Disable Next button if Date is Current
        today = datetime.now().strftime("%B %d, %Y")
        if self.current_date.get() == today:
            self.btn_date_next.config(state="disabled")

    def add_entry_win(self):
        self.add_window = tk.Toplevel(self)
        self.add_window.title("Add Items")
        self.add_window.geometry("400x300")
        self.add_window.config(bg="#102C57")

        frame = tk.Frame(self.add_window, bg="#EADBC8", width=340, height=230)
        frame.place(x=30, y=30)

        ttk.Label(frame, text="Category:", font=("katibeh", 16, "bold"), background="#EADBC8").place(x=10, y=20)
        ttk.Label(frame, text="Name:", font=("katibeh", 16, "bold"), background="#EADBC8").place(x=10, y=60)
        ttk.Label(frame, text="Amount:", font=("katibeh", 16, "bold"), background="#EADBC8").place(x=10, y=100)

        self.ent_category = ttk.Combobox(frame, values=["Income", "Expense"], font=("katibeh", 16), width=12)
        self.ent_category.set("Expense")
        self.ent_name = ttk.Entry(frame, font=("katibeh", 16), width=16)
        self.ent_amount = ttk.Entry(frame, font=("katibeh", 16), width=14)

        self.ent_category.place(x=130, y=20)
        self.ent_name.place(x=90, y=60)
        self.ent_amount.place(x=110, y=100)

        btn_add = tk.Button(frame, text="Add", font=("katibeh", 16), width=9, command=self.add_to_db)
        btn_add.place(x=120, y=170)


    def previous_date(self):
        current = datetime.strptime(self.current_date.get(), "%B %d, %Y")
        new_date = current - timedelta(days=1)
        self.current_date.set(new_date.strftime("%B %d, %Y"))
        # Enable the "Next" button if it was disabled before
        self.btn_date_next.config(state="normal")
        self.load_entries()
        self.update_amount_label()

    def next_date(self):
        current = datetime.strptime(self.current_date.get(), "%B %d, %Y")
        new_date = current + timedelta(days=1)
        self.current_date.set(new_date.strftime("%B %d, %Y"))
        # Check if the current date is today, if yes, disable the "Next" button
        today = datetime.now().strftime("%B %d, %Y")
        if self.current_date.get() == today:
            self.btn_date_next.config(state="disabled")
        self.load_entries()
        self.update_amount_label()

    def load_entries(self):
        # Get current date
        current_date = self.current_date.get()

        # Load entries from the database for the current date
        self.entries = db.load_entries(current_date)

        # Clear existing entries in the Treeview
        for record in self.tv_tree_view.get_children():
            self.tv_tree_view.delete(record)

        # Insert loaded entries into the Treeview
        if self.entries:
            for entry in self.entries:
                # Extract entry details
                category = entry[2]
                amount = entry[4]

                # Format amount based on category
                if category == "Expense":
                    formatted_amount = "-₱{:.2f}".format(abs(amount))  # Display negative amount
                    text_color = "#FF0000"  # Red for expenses
                elif category == "Income":
                    formatted_amount = "+₱{:.2f}".format(abs(amount))  # Display positive amount
                    text_color = "#006400"  # Green for income
                else:
                    formatted_amount = "₱{:.2f}".format(amount)  # Default format
                    text_color = "#000000"  # Default color

                # Insert the entry into the Treeview with appropriate color and tag
                formatted_entry = (entry[1], entry[3], formatted_amount)  # Update amount in entry
                self.tv_tree_view.insert('', 'end', values=formatted_entry, tags=(category,))
                # Apply the color to the entire row
                self.tv_tree_view.tag_configure(category, foreground=text_color)

        self.update_amount_label()
    def update_amount_label(self):
        total_expenses = 0
        total_income = 0
        if self.entries:
            for entry in self.entries:
                category = entry[2]
                amount = entry[4]

                if category == "Expense":
                    total_expenses += amount
                elif category == "Income":
                    total_income += amount

            # Update the expenses and income labels with the calculated totals
            self.lbl_expenses_amount.config(text="₱{:.2f}".format(total_expenses))
            self.lbl_income_amount.config(text="₱{:.2f}".format(total_income))
            self.update_total_balance()

        else:
            self.lbl_expenses_amount.config(text="₱{:.2f}".format(total_expenses))
            self.lbl_income_amount.config(text="₱{:.2f}".format(total_income))

    def update_total_balance(self):
        total_balance = db.total_amount()
        if total_balance is not None:  # Check if total_balance is not None
            self.lbl_amount_amount.config(text="₱{:.2f}".format(total_balance))
        else:
            self.lbl_amount_amount.config(text="₱0.00")


    def add_to_db(self):
        date = self.current_date.get()
        category = self.ent_category.get()
        name = self.ent_name.get()         
        amount = self.ent_amount.get() 

        if date and category and amount:
            try:
                amount = float(amount)               
                db.add_data_to_table(date, category, name, amount)

                self.add_window.destroy()
                self.load_entries()
                self.update_total_balance()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount")
        else:
            messagebox.showerror("Error", "Please fill in all fields")


# Call StartUp
# app = StartUp()
# app.mainloop()

# Call Main Window
win = MyApp()
win.mainloop()
