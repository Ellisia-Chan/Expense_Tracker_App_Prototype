import db
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x600+0+0")
        self.title("Pera ko")
        self.resizable(False, False)

        db.create_database()
        self.chart_open = False # Need Sa __init__ ===================================
        
        # Call Methods
        self.create_widgets()
        self.load_entries()
        self.update_total_balance()
    # --------------------------- Sa loob ng Create Widgets--------------------------------   
    # Show Records or Charts in main window
    def show_records(self):
        self.mid_frame.place(x=0, y=130)
        self.top_frame.config(height=130)
        self.lbl_date.place(x=140, y=50)
        self.lbl_expenses.place(x=440, y=30)
        self.lbl_income.place(x=580, y=30)
        self.lbl_balance.place(x=730, y=30)

        self.lbl_expenses_amount.place(x=440, y=60)
        self.lbl_income_amount.place(x=580, y=60)
        self.lbl_amount_amount.place(x=730, y=60)

        self.btn_date_next.place(x=320, y=50)
        self.btn_date_previous.place(x=80, y=50)
        
        self.btn_add.config(state="normal")
        
        long_char_dates = ["January", "February", "August", "September", "October", "November", "December"]

        if self.current_date.get().split()[0] in long_char_dates:
            self.btn_date_next.place(x=370, y=50)
        else:
            self.lbl_date.place(x=140, y=50)
            self.btn_date_next.place(x=320, y=50)
        
        self.close_chart()
        self.chart_frame.place_forget()

        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview.Heading", font=("katibeh", 18))
        style.configure("Custom.Treeview", font=("katibeh", 18), background="#EADBC8", fieldbackground="#EADBC8")
        style.configure("Custom.Treeview", rowheight=40)
        
    
    def show_chart(self):
        # Disable Add Entry Btn
        self.btn_add.config(state="disabled")
        
        # Frame pos
        self.chart_frame.place(x=0, y=60)
        
        # Chart Frame Widgets
        months = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        
        year = []
        
        current_month_number = datetime.now().month
        current_month_name = datetime.now().strftime('%B')
        current_year = datetime.now().year
        current_year_str = str(current_year)
        
        # Add year to the list for Combobox selection
        year.append(current_year_str) if current_year_str not in year else None
   
        self.chart_month = ttk.Combobox(
            self.chart_frame,
            values=months,
            font=("katibeh", 16),
            width=16,
            state="readonly"
        )
        self.chart_month.set(current_month_name)
        self.chart_month.bind("<<ComboboxSelected>>", self.create_chart_and_add_entries)
        
        self.chart_year = ttk.Combobox(
            self.chart_frame,
            values=year,
            font=("katibeh", 16),
            width=12,
            state="readonly"
        )
        self.chart_year.set(current_year_str)
        self.chart_year.bind("<<ComboboxSelected>>", self.create_chart_and_add_entries)
        
        # Chart Frame Widgets pos
        self.chart_month.place(x=20, y=20)
        self.chart_year.place(x=250, y=20)
        # Treeview Expense
        lbl_expense = tk.Label(
            self.chart_frame,
            text="Expenses",
            font=("katibeh", 18),
            bg="#EADBC8"
        ).place(x=480, y=10)
        
        self.tv_chart_expense = ttk.Treeview(
            self.chart_frame,
            columns=(1, 2),
            show="headings",
            height=9,
            style="Custom.Treeview"
        )        
        
        self.tv_chart_expense.column(1, anchor="w", stretch="No", width=110)
        self.tv_chart_expense.column(2, anchor="w", stretch="No", width=110)
        self.tv_chart_expense.heading(1, text="Name")
        self.tv_chart_expense.heading(2, text="Amount")
        
        # Disable TreeView Heading Resizing and selection
        self.tv_chart_expense.bind('<B1-Motion>', lambda event: 'break')
        self.tv_chart_expense.bind("<ButtonRelease-1>", lambda event: self.tv_tree_view.selection_remove(self.tv_tree_view.selection()))

        # TreeView Expense pos
        self.tv_chart_expense.place(x=420, y=50)
        
        # Treeview Income
        lbl_chart_income = tk.Label(
            self.chart_frame,
            text="Income",
            font=("katibeh", 18),
            bg="#EADBC8"
        ).place(x=720, y=10)
        
        self.tv_chart_income = ttk.Treeview(
            self.chart_frame,
            columns=(1, 2),
            show="headings",
            height=9,
            style="Custom.Treeview"
        )
        
        self.tv_chart_income.column(1, anchor="w", stretch="No", width=110)
        self.tv_chart_income.column(2, anchor="w", stretch="No", width=110)
        self.tv_chart_income.heading(1, text="Name")
        self.tv_chart_income.heading(2, text="Amount")
        
        # Disable TreeView Heading Resizing and selection
        self.tv_chart_income.bind('<B1-Motion>', lambda event: 'break')
        self.tv_chart_income.bind("<ButtonRelease-1>", lambda event: self.tv_tree_view.selection_remove(self.tv_tree_view.selection()))
        
        # TreeView Income pos
        self.tv_chart_income.place(x=660, y=50)
        
        # Config TreeView Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview.Heading", font=("katibeh", 16))
        style.configure("Custom.Treeview", font=("katibeh", 12), background="#EADBC8", fieldbackground="#EADBC8")
        style.configure("Custom.Treeview", rowheight=40)
    
        # Create Chart and add List of Income and Expenses
        # if chart have no data
        self.lbl_no_data = tk.Label(
            self.chart_frame,
            text="No Data",
            font=("katibeh", 30)
        )
        
        self.create_chart_and_add_entries()
        
    # -------------------------------- Function For Chart ---------------------------------------------    
    # Create Chart and Add entries into treeView in Chart Frame
    def create_chart_and_add_entries(self, event=None):
        total_income, total_expenses = db.get_income_expense_total(self.chart_month.get(), self.chart_year.get())
        
        if self.chart_open:
            self.ax.clear()
        else:
            # Create a new figure and axis if the chart is not open
            self.fig, self.ax = plt.subplots(figsize=(4, 4))  # Adjust the figsize to make the chart smaller
            self.chart_open = True
        
        # Clear canvas if it's open
        if hasattr(self, 'canvas'):
            self.canvas.get_tk_widget().place_forget()
        
        # Create a canvas to display the Matplotlib chart
        canvas = FigureCanvasTkAgg(self.fig, master=self.chart_frame)
        
        # Get Data and Set to No data if None
        if total_income == 0 and total_expenses == 0:
            # No data available, show the "No data" label
            self.lbl_no_data.place(x=100, y=70)
        else:
            # Data available, hide the "No data" label
            self.lbl_no_data.place_forget()
            
            expenses_percentage = (total_expenses / (total_expenses + total_income)) * 100
            income_percentage = (total_income / (total_expenses + total_income)) * 100

            # Create pie chart
            labels = ['Expenses', 'Income']
            sizes = [expenses_percentage, income_percentage]
            colors = ['#ff9999', '#66b3ff']

            self.ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
            self.ax.axis('equal')
            self.ax.set_title(f'Percentage of Expenses and Income in {self.chart_month.get()} {self.chart_year.get()}', fontsize=11)

        canvas.get_tk_widget().place(x=10, y=60) # Position the chart 
        canvas.draw()

        # Insert Entries in the Expense/Income TreeView
        income_list = db.get_income_list(self.chart_month.get(), self.chart_year.get())
        expense_list = db.get_expense_list(self.chart_month.get(), self.chart_year.get())
        
        for record in self.tv_chart_income.get_children():
            self.tv_chart_income.delete(record)
            
        for record in self.tv_chart_expense.get_children():
            self.tv_chart_expense.delete(record)
        
        if income_list:   
            for income in income_list:
                name = income[3]
                amount = income[4]
                
                formatted_amount = "+₱{:.2f}".format(abs(amount))
                
                formatted_entry = (name, formatted_amount)
                self.tv_chart_income.insert('', 'end', values=formatted_entry, tags=(name))
                self.tv_chart_income.tag_configure(name, foreground="#006400")
        
        if expense_list:
            for expenses in expense_list:
                name = expenses[3]
                amount = expenses[4]
                
                formatted_amount = "-₱{:.2f}".format(abs(amount))
                
                formatted_entry = (name, formatted_amount)
                self.tv_chart_expense.insert('', 'end', values=formatted_entry, tags=(name))
                self.tv_chart_expense.tag_configure(name, foreground="#FF0000")
            



                                                         
    def close_chart(self):
        if self.chart_open:
            plt.close(self.fig)
            self.chart_open = False  
    
    def exit_program(self):
        self.close_chart()
        self.destroy()   
