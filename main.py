import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta


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

        AppFunction(self)

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

        # Top Frame widgets
        # Lbl
        self.lbl_date = tk.Label(self.top_frame, textvariable=self.current_date, font=("katibeh", 20, "bold"), bg="#102C57",
                                 fg="#fff")
        lbl_expenses = tk.Label(self.top_frame, text="Expenses", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff")
        lbl_income = tk.Label(self.top_frame, text="Income", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff")
        lbl_balance = tk.Label(self.top_frame, text="Balance", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff")

        self.lbl_expenses_amount = tk.Label(self.top_frame, text="₱1,000,000", font=("katibeh", 14, "bold"),
                                            bg="#102C57",
                                            fg="#FF0000")
        self.lbl_income_amount = tk.Label(self.top_frame, text="₱1,000,000", font=("katibeh", 14, "bold"), bg="#102C57",
                                          fg="#90EE90")
        self.lbl_amount_amount = tk.Label(self.top_frame, text="₱1,000,000", font=("katibeh", 14, "bold"), bg="#102C57",
                                          fg="#fff")

        # Btn
        btn_menu = tk.Button(self.top_frame, text="≡", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff", width=3)
        btn_search = tk.Button(self.top_frame, text="🔍", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff", width=3)

        btn_date_next = tk.Button(self.top_frame, text=">", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff",
                                  width=3, command=AppFunction(self).next_date)
        btn_date_previous = tk.Button(self.top_frame, text="<", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff",
                                      width=3, command=AppFunction(self).previous_date)

        # Top Frame Widgets pos
        # lbl
        self.lbl_date.place(x=160, y=50)
        lbl_expenses.place(x=40, y=110)
        lbl_income.place(x=210, y=110)
        lbl_balance.place(x=360, y=110)

        self.lbl_expenses_amount.place(x=30, y=140)
        self.lbl_income_amount.place(x=200, y=140)
        self.lbl_amount_amount.place(x=350, y=140)

        # Btn
        btn_menu.place(x=10, y=10)
        btn_search.place(x=450, y=10)

        btn_date_next.place(x=360, y=50)
        btn_date_previous.place(x=100, y=50)

        # Mid Frame widgets
        # TreeView
        self.tv_tree_view = ttk.Treeview(self.mid_frame, columns=(1, 2), show="headings", height=23)
        self.tv_tree_view.column(1, anchor="center", stretch="No", width=240)
        self.tv_tree_view.column(2, anchor="center", stretch="No", width=240)
        self.tv_tree_view.heading(1, text="Name")
        self.tv_tree_view.heading(2, text="Amount")

        # Mid Frame Pos
        self.tv_tree_view.pack(side="left")

        # Tree View Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Helvetica", 18))
        style.configure("Treeview", font=("Helvetica", 14), background="#EADBC8", fieldbackground="#EADBC8")

        self.tv_tree_view.bind('<Button-1>', 'break')

        scrollbar = ttk.Scrollbar(self.mid_frame, orient="vertical")
        scrollbar.configure(command=self.tv_tree_view.yview())
        scrollbar.pack(side="right", fill="y")

class AppFunction:
    def __init__(self, my_app):
        self.win_widgets = my_app
        self.current_date = my_app.current_date

    def previous_date(self):
        current = datetime.strptime(self.current_date.get(), "%B %d, %Y")
        new_date = current - timedelta(days=1)
        self.current_date.set(new_date.strftime("%B %d, %Y"))

    def next_date(self):
        current = datetime.strptime(self.current_date.get(), "%B %d, %Y")
        new_date = current + timedelta(days=1)
        self.current_date.set(new_date.strftime("%B %d, %Y"))
     
    

# Call StartUp
# app = StartUp()
# app.mainloop()

# Call Main Window
win = MyApp()
win.mainloop()
