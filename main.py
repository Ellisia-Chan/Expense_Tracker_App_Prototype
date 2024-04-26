import tkinter as tk


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

    def create_widgets(self):
        # Frames
        self.top_frame = tk.Frame(self, width=500, height=180, bg="#102C57")
        self.mid_frame = tk.Frame(self, width=500, height=490, bg="#EADBC8")
        self.bot_frame = tk.Frame(self, width=500, height=80, bg="#102C57")

        # Frames pos
        self.top_frame.place(x=0, y=0)
        self.mid_frame.place(x=0, y=180)
        self.bot_frame.place(x=0, y=670)

        # Top Frame widgets
        # Lbl
        lbl_date = tk.Label(self.top_frame, text="Date Here", font=("katibeh", 20, "bold"), bg="#102C57", fg="#fff")
        lbl_expenses = tk.Label(self.top_frame, text="Expenses", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff")
        lbl_income = tk.Label(self.top_frame, text="Income", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff")
        lbl_balance = tk.Label(self.top_frame, text="Balance", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff")

        lbl_expenses_amount = tk.Label(self.top_frame, text="₱1,000,000", font=("katibeh", 14, "bold"), bg="#102C57",
                                       fg="#FF0000")
        lbl_income_amount = tk.Label(self.top_frame, text="₱1,000,000", font=("katibeh", 14, "bold"), bg="#102C57",
                                     fg="#90EE90")
        lbl_amount_amount = tk.Label(self.top_frame, text="₱1,000,000", font=("katibeh", 14, "bold"), bg="#102C57",
                                     fg="#fff")

        # Btn
        btn_menu = tk.Button(self.top_frame, text="≡", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff", width=3)
        btn_search = tk.Button(self.top_frame, text="🔍", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff", width=3)

        btn_date_next = tk.Button(self.top_frame, text=">", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff",
                                  width=3)
        btn_date_previous = tk.Button(self.top_frame, text="<", font=("katibeh", 14, "bold"), bg="#102C57", fg="#fff",
                                      width=3)

        # Top Frame Widgets pos
        # lbl
        lbl_date.place(x=185, y=50)
        lbl_expenses.place(x=40, y=110)
        lbl_income.place(x=210, y=110)
        lbl_balance.place(x=360, y=110)

        lbl_expenses_amount.place(x=30, y=140)
        lbl_income_amount.place(x=200, y=140)
        lbl_amount_amount.place(x=350, y=140)

        # Btn
        btn_menu.place(x=10, y=10)
        btn_search.place(x=450, y=10)

        btn_date_next.place(x=340, y=50)
        btn_date_previous.place(x=120, y=50)

        # Mid Frame widgets
        lb_listbox = tk.Listbox(self.mid_frame, width=44, height=30, borderwidth=0, highlightthickness=0,
                                font=("katibeh", 14, "bold"), bg="#EADBC8")

        # Mid Frame Widgets pos
        lb_listbox.place(x=10, y=10)


# Call StartUp
# app = StartUp()
# app.mainloop()

# Call Main Window
win = MyApp()
win.mainloop()
