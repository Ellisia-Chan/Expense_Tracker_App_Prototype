# Customized GUI made from figma, credits to the Tkinter Designer by Parth Jadhav to generate the file
# https://github.com/ParthJadhav/Tkinter-Designer


import tkinter as tk
import db
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, ttk, messagebox
from datetime import datetime, timedelta



# Seperate file for the app functions
import function_list as fl
from currency_conv import CurrencyConverter
from calc import Calculator


# Loading screen class
class LoadingScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)

        # Center LoadingScreen Window
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry("+{}+{}".format(x, y))

        # Call methods
        self.loading_screen()
        self.loading(0)

    # Loading screen of the app 
    def loading_screen(self):
        # Frame
        self.frame_parent = tk.Frame(
            self,
            width=500,
            height=200,
            bd=10,
            relief=tk.GROOVE,
            bg="#102C57"
        )
        
        self.frame_child = tk.Frame(
            self.frame_parent,
            width=480,
            height=180,
            bd=5,
            relief=tk.GROOVE,
            bg="#EADBC8"
        )
        
      # Lbl
        lbl_title = tk.Label(
            self.frame_child,
            text="Pera Ko",
            font=("kuashan script", 40, "bold"),
            bg="#EADBC8"
        )

        self.lbl_loading = tk.Label(
            self.frame_child,
            text="0 %",
            font=("kuashan script", 18, "bold"),
            bg="#EADBC8"
        )
        
        # Widget Pos
        # Frame
        self.frame_parent.pack()
        self.frame_child.place(x=5, y=5)
        
        # Lbl        
        lbl_title.place(x=130, y=50)
        self.lbl_loading.place(x=200, y=120)
        
    # Loading Progress Counter
    def loading(self, progress):
        if progress <= 100:
            self.lbl_loading.config(text=f"{progress} %")
            progress += 1
            self.after(2, self.loading, progress)
        else:
            self.destroy()
            window = MyApp()
            window.mainloop()

# Class for the main application
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()          
        # Path directory to access assets
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / "assets"  # Adjust this path according to your project structure
        
        # Initiate tkinter base frame of the app
        self.geometry("700x600")
        self.configure(bg="#FFFFFF")
        self.title("Pera ko, a money tracker app made by Group 4")

        # Check if Database exist, if not, create database file where the py file is located.
        db.create_database()
        
        self.canvas()
        # self.load_entries()
        # self.update_total_balance()
        
        
    # Canvas to create the base frame of the app        
    def canvas(self):
        self.canvas = Canvas(self, bg="#FFFFFF", height=600, width=700, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # Background color
        self.bg_color_img = PhotoImage(file=self.relative_to_assets("bg_color.png"))
        self.bg_color = self.canvas.create_image(350.0, 310.0, image=self.bg_color_img)

        # Flower background
        self.bg_flower1_img = PhotoImage(file=self.relative_to_assets("bg_flower1.png"))
        self.bg_flower1 = self.canvas.create_image(277, 291, image=self.bg_flower1_img)

        # Bottom background frame w/ shadow
        self.bg_bottom_frame_img = PhotoImage(file=self.relative_to_assets("bg_bottom_frame.png"))
        self.bg_bottom_frame = self.canvas.create_image(350.0, 559.5, image=self.bg_bottom_frame_img)

        # Mid frame for treeview
        self.mid_frame = tk.Frame(self, width=550, height=630, bg="red")
        self.mid_frame.place(x=10, y=85)
        
        
        # Top background frame w/ shadow
        self.bg_top_frame_img = PhotoImage(file=self.relative_to_assets("bg_top_frame.png"))
        self.bg_top_frame = self.canvas.create_image(350.0, 39.0, image=self.bg_top_frame_img)

        # Flower background (design on top of top & bottom background frame)
        self.bg_flower2_img = PhotoImage(file=self.relative_to_assets("bg_flower2.png"))
        self.bg_flower2 = self.canvas.create_image(533, 36, image=self.bg_flower2_img)


        self.bg_flower3_img = PhotoImage(file=self.relative_to_assets("bg_flower3.png"))
        self.bg_flower3 = self.canvas.create_image(120, 577, image=self.bg_flower3_img)


        self.bg_flower4_img = PhotoImage(file=self.relative_to_assets("bg_flower4.png"))
        self.bg_flower4 = self.canvas.create_image(573, 551, image=self.bg_flower4_img)


        self.bg_flower5_img = PhotoImage(file=self.relative_to_assets("bg_flower5.png"))
        self.bg_flower5 = self.canvas.create_image(357, 51, image=self.bg_flower5_img)


        self.bg_flower6_img = PhotoImage(file=self.relative_to_assets("bg_flower6.png"))
        self.bg_flower6 = self.canvas.create_image(677, 48, image=self.bg_flower6_img)


        # -------------------------------------Top widgets-------------------------------------#

        # Date Label
        self.current_date = tk.StringVar()
        self.current_date.set(datetime.now().strftime("%B %d, %Y"))
        self.current_date_id = self.canvas.create_text(130.0, 35.0, anchor="center", text=self.current_date.get(), fill="#CA0000", font=("AbrilFatface Regular", 20 * -1))
        

        # Date button left (<)
        self.btn_date_left_img = PhotoImage(file=self.relative_to_assets("btn_date_left.png"))
        self.btn_date_left = Button(image=self.btn_date_left_img, borderwidth=0, highlightthickness=0,
                                    command=self.previous_date, relief="flat")
        self.btn_date_left.place(x=15.0, y=26.0, width=26.0, height=26.0)

        # Date button right (>)
        self.btn_date_right_img = PhotoImage(file=self.relative_to_assets("btn_date_right.png"))
        self.btn_date_right = Button(image=self.btn_date_right_img, borderwidth=0, highlightthickness=0,
                                     command=self.next_date, relief="flat")
        self.btn_date_right.place(x=218.0, y=26.0, width=26.0, height=26.0)

        # Expense Label
        self.lbl_expense_amount_img = PhotoImage(file=self.relative_to_assets("lbl_expense_amount.png"))
        self.lbl_expense_amount = self.canvas.create_image(324.0, 26.0, image=self.lbl_expense_amount_img)
        self.canvas.create_text(287.0, 49.0, anchor="nw", text="₱6,000.00", fill="#CA0000", font=("AbrilFatface Regular", 15 * -1))

        # Income Label
        self.lbl_income_amount_img = PhotoImage(file=self.relative_to_assets("lbl_income_amount.png"))
        self.lbl_income_amount = self.canvas.create_image(467.0, 26.0, image=self.lbl_income_amount_img)
        self.canvas.create_text(430.0, 49.0, anchor="nw", text="₱6,000.00", fill="#005D0B", font=("AbrilFatface Regular", 15 * -1))

        # Balance Label
        self.lbl_balance_amount_img = PhotoImage(file=self.relative_to_assets("lbl_balance_amount.png"))
        self.lbl_balance_amount = self.canvas.create_image(611.0, 26.0, image=self.lbl_balance_amount_img)
        self.canvas.create_text(573.0, 49.0, anchor="nw", text="₱6,000.00", fill="#CA0000", font=("AbrilFatface Regular", 15 * -1))



        # -------------------------------------Mid widgets-------------------------------------#
        
        # Display tree view frame
        self.tv_tree_view = ttk.Treeview( self.mid_frame, columns=(1, 2, 3), show="headings", height=12, style="Custom.Treeview")
        
        # TreeView columns and headings
        self.tv_tree_view.column(1, anchor="center", stretch="No", width=120)
        self.tv_tree_view.column(2, anchor="center", stretch="No", width=250)
        self.tv_tree_view.column(3, anchor="center", stretch="No", width=150)
        self.tv_tree_view.heading(1, text="ID")
        self.tv_tree_view.heading(2, text="Name")
        self.tv_tree_view.heading(3, text="Amount")

        # TreeView position
        self.tv_tree_view.pack(side="left")

        # Configure TreeView Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview.Heading", font=("katibeh", 18))
        style.configure("Custom.Treeview", font=("katibeh", 16), background="#EADBC8", fieldbackground="#EADBC8")
        style.configure("Custom.Treeview", rowheight=30)

        # Disable TreeView Heading Resizing and selection
        self.tv_tree_view.bind('<B1-Motion>', lambda event: 'break')
        self.tv_tree_view.bind("<ButtonRelease-1>", lambda event: self.tv_tree_view.selection_remove(self.tv_tree_view.selection()))

        # TreeView Vertical ScrollBar
        scrollbar = ttk.Scrollbar(self.mid_frame, orient="vertical", command=self.tv_tree_view.yview)
        scrollbar.pack(side="right", fill="y")
        
        
        
        # -------------------------------------Bottom widgets-------------------------------------#

        # Menu button
        self.btn_menu_img = PhotoImage(file=self.relative_to_assets("btn_menu.png"))
        self.btn_menu = Button(image=self.btn_menu_img, borderwidth=0, highlightthickness=0,
                               command=lambda: print("btn_menu clicked"), relief="flat")
        self.btn_menu.place(x=7.0, y=525.0, width=70.0, height=70.0)

        # Analysis button
        self.btn_analysis_img = PhotoImage(file=self.relative_to_assets("btn_analysis.png"))
        self.btn_analysis = Button(image=self.btn_analysis_img, borderwidth=0, highlightthickness=0,
                                   command=lambda: print("btn_analysis clicked"), relief="flat")
        self.btn_analysis.place(x=175.0, y=525.0, width=70.0, height=70.0)

        # Accounts button
        self.btn_accounts_img = PhotoImage(file=self.relative_to_assets("btn_accounts.png"))
        self.btn_accounts = Button(image=self.btn_accounts_img, borderwidth=0, highlightthickness=0,
                                   command=lambda: print("btn_accounts clicked"), relief="flat")
        self.btn_accounts.place(x=315.0, y=525.0, width=70.0, height=70.0)

        # Records button
        self.btn_records_img = PhotoImage(file=self.relative_to_assets("btn_records.png"))
        self.btn_records = Button(image=self.btn_records_img, borderwidth=0, highlightthickness=0,
                                  command=lambda: print("btn_records clicked"), relief="flat")
        self.btn_records.place(x=455.0, y=525.0, width=70.0, height=70.0)

        # Search button
        self.btn_search_img = PhotoImage(file=self.relative_to_assets("btn_search.png"))
        self.btn_search = Button(image=self.btn_search_img, borderwidth=0, highlightthickness=0,
                                 command=lambda: print("btn_search clicked"), relief="flat")
        self.btn_search.place(x=617.0, y=525.0, width=70.0, height=70.0)


    
        # -------------------------------------Right widgets-------------------------------------#

        # Currency exchange button
        self.btn_currency_img = PhotoImage(file=self.relative_to_assets("btn_currency.png"))
        self.btn_currency = Button( image=self.btn_currency_img, borderwidth=0, highlightthickness=0, 
                        command=self.open_currency_converter, relief="flat")
        self.btn_currency.place(x=584.0, y=95.0, width=102.0, height=103.)


        # Calculator button
        self.btn_calculator_img = PhotoImage(file=self.relative_to_assets("btn_calculator.png"))
        self.btn_calculator = Button(image=self.btn_calculator_img, borderwidth=0, highlightthickness=0, 
                        command=self.open_calculator, relief="flat")
        self.btn_calculator.place( x=585.0, y=198.0, width=102.0, height=102.0)


        # Update Edit button
        self.btn_edit_img = PhotoImage(file=self.relative_to_assets("btn_edit.png"))
        self.btn_edit = Button( image=self.btn_edit_img, borderwidth=0, highlightthickness=0, 
                        command=self.edit_button, relief="flat")
        
        self.btn_edit.place( x=584.0, y=300.0, width=102.0, height=103. )


        # Add button
        self.btn_add_item_img = PhotoImage(file=self.relative_to_assets("btn_add_item.png"))
        self.btn_add_item = Button(image=self.btn_add_item_img, borderwidth=0, highlightthickness=0,
                        command=self.add_button, relief="flat")
        self.btn_add_item.place(x=585.0, y=403.0, width=102.0, height=102.0)

        # Condition For Buttons for Changing Months
        today = datetime.now().strftime("%B %d, %Y")
        if self.current_date.get() == today:
            self.btn_date_right.config(state="disabled")


    # Get access to the asset files from directory path
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    # Next Date
    def next_date(self):
        # Get current date displayed and add one day to get next date
        current = datetime.strptime(self.current_date.get(), "%B %d, %Y")
        new_date = current + timedelta(days=1)
        self.current_date.set(new_date.strftime("%B %d, %Y"))
        
        # Update canvas text
        self.canvas.itemconfig(self.current_date_id, text=self.current_date.get())
        
        # Check if the current date is today, if yes, disable the "Next" button
        today = datetime.now().strftime("%B %d, %Y")
        if self.current_date.get() == today:
            self.btn_date_right.config(state="disabled")
        
    def previous_date(self):
        # Get current date displayed and add one day to get next date
        current = datetime.strptime(self.current_date.get(), "%B %d, %Y")
        new_date = current - timedelta(days=1)
        self.current_date.set(new_date.strftime("%B %d, %Y"))
        
        # Update canvas text
        self.canvas.itemconfig(self.current_date_id, text=self.current_date.get())
        self.btn_date_right.config(state="normal")
    
    # Load Data to Treeview
    def load_entries(self):
        formatted_entries= fl.LoadEntries(self, self.current_date.get())
        formatted_entry, text_color, category = formatted_entries.get_entries()
        
        for record in self.tv_tree_view.get_children():
            self.tv_tree_view.delete(record)
            
        # Insert the entry into the Treeview with appropriate color and tag
        self.tv_tree_view.insert('', 'end', values=formatted_entry, tags=(category,))
        self.tv_tree_view.tag_configure(category, foreground=text_color)
            
    # Open Window for Calculator and Currency Calculator py file
    def open_calculator(self):
        Calculator(self)
    
    def open_currency_converter(self):
        CurrencyConverter(self)
        
    # Wrapper functions to call imported functions from function_list.py
    def add_button(self):
        fl.AddEntryWindow(self)
        self.load_entries()
        
    def edit_button(self):
        fl.EditEntriesWindow(self)
        
    
    
    


# Start the program
if __name__ == "__main__":
    # app = LoadingScreen()
    # app.mainloop()
    app = MyApp()
    app.mainloop()
