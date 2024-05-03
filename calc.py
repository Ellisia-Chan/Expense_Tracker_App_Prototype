import re
import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.app = root
        self.win = tk.Toplevel(self.app)
        self.win.grab_set()
        self.win.geometry("500x500")
        self.win.title("Calculator")
        self.win.resizable(False, False)
        self.win.protocol("WM_DELETE_WINDOW", self.back_to_main)

        self.create_widgets()
        
    def create_widgets(self):
        # Frame
        parent_frame = tk.Frame(self.win, width=500, height=500, bg="#102C57")
        child_frame = tk.Frame(self.win, width=460, height=460, bg="#EADBC8")
        
        # Ent
        self.ent_num_field = tk.Entry(
            child_frame,
            font=("katibeh", 26),
            width=22,
            justify="right"
        )
        
        self.ent_num_field.config(validate="key", validatecommand=(self.ent_num_field.register(lambda char: char.isdigit() or char == "" or char in "-+÷%.x(()"), "%S"))

        
        # Btn
        # Back Button
        btn_back = tk.Button(
            child_frame,
            text="<",
            font=("katibeh", 14, "bold"),
            bg="#102C57",
            fg="#fff",
            cursor="hand2",
            width=5,
            command=self.back_to_main
        )
        
        # Btn Row 1
        btn_open_parenthesis = tk.Button(
            child_frame,
            text="(",
            font=("katibeh", 18),
            width=5,
            command=lambda: self.ent_num_field.insert(tk.END, "(")
        )
        
        btn_close_parenthesis = tk.Button(
            child_frame,
            text=")",
            font=("katibeh", 18),
            width=5,
            command=lambda: self.ent_num_field.insert(tk.END, ")")
        )
        
        btn_ac = tk.Button(
            child_frame,
            text="AC",
            font=("katibeh", 18),
            width=5,
            command=self.clear
        )
        
        btn_del = tk.Button(
            child_frame,
            text="Del",
            font=("katibeh", 18),
            width=5,
            command=self.delete
        )
        
        # Btn Row 2       
        btn_7 = tk.Button(
            child_frame,
            text="7",
            font=("katibeh", 18),
            width=5,
            command=lambda: self.ent_num_field.insert(tk.END, "7")
        )
        
        btn_8 = tk.Button(
            child_frame,
            text="8"  ,
            font=("katibeh", 18),
            width=5,
            command=lambda: self.ent_num_field.insert(tk.END, "8")
        )
        
        btn_9 = tk.Button(
            child_frame,
            text=9,
            font=("katibeh", 18),
            width=5,
            command=lambda: self.ent_num_field.insert(tk.END, "9")
        )
        
        btn_divide = tk.Button(
            child_frame,
            text="÷",
            font=("katibeh", 18),
            width=5,
            command=lambda: self.ent_num_field.insert(tk.END, "÷")
        )
        
        # Btn Row 3
        btn_4 = tk.Button(
            child_frame,
            text="4",
            font=("katibeh", 18),
            width=5,
            command=lambda: self.ent_num_field.insert(tk.END, "4")
        )
        
        btn_5 = tk.Button(
            child_frame,
            text="5",
            font=("katibeh", 18),
            width=5,
            command=lambda: self.ent_num_field.insert(tk.END, "5")
        )
        
        btn_6 = tk.Button(
            child_frame,
            text="6",
            font=("katibeh", 18),
            width=5,
            command=lambda: self.ent_num_field.insert(tk.END, "6")
        )
        
        btn_multiply = tk.Button(
            child_frame,
            text="x",
            font=("katibeh", 18),
            width=5,
            command=lambda: self.ent_num_field.insert(tk.END, "x")
        )
        
        # Btn Row 4
        btn_1 = tk.Button(
            child_frame,
            text="1",
            font=("katibeh", 18),
            width=5,
            command=lambda: self.ent_num_field.insert(tk.END, "1")
        )
        
        btn_2 = tk.Button(
            child_frame,
            text="2",
            font=("katibeh", 18),
            width=5,
            command=lambda: self.ent_num_field.insert(tk.END, "2")
        )
        
        btn_3 = tk.Button(
            child_frame,
            text="3",
            font=("katibeh", 18),
            width=5,
            command=lambda: self.ent_num_field.insert(tk.END, "3")
        )
        
        btn_subtract = tk.Button(
            child_frame,
            text="-",
            font=("katibeh", 18),
            width=5,
            command=lambda: self.ent_num_field.insert(tk.END, "-")
        )
        
        # Btn Row 5
        btn_0 = tk.Button(
            child_frame,
            text="0",
            font=("katibeh", 18),
            width=12,
            command=lambda: self.ent_num_field.insert(tk.END, "0")
        )        
        
        btn_equal = tk.Button(
            child_frame,
            text="=",
            font=("katibeh", 18),
            bg="#90EE90",
            width=5,
            command=self.calculate
        )
        
        btn_addition = tk.Button(
            child_frame,
            text="+",
            font=("katibeh", 18),
            width=5,
            command=lambda: self.ent_num_field.insert(tk.END, "+")
        )
        
        # Widgets Pos
        # Frame pos
        parent_frame.place(x=0, y=0)
        child_frame.place(x=20, y=20)
        
        # Ent pos
        self.ent_num_field.place(x=20, y=50)
        
        # Btn pos
        # Back Button
        btn_back.place(x=10, y=5)
        
        # Btn Row 1
        btn_open_parenthesis.place(x=40, y=120)
        btn_close_parenthesis.place(x=140, y=120)
        btn_ac.place(x=240, y=120)
        btn_del.place(x=340, y=120)
        
        
        # Btn Row 2
        btn_7.place(x=40, y=190)
        btn_8.place(x=140, y=190)
        btn_9.place(x=240, y=190)
        btn_divide.place(x=340, y=190)
        
        # Btn Row 3
        btn_4.place(x=40, y=260)
        btn_5.place(x=140, y=260)
        btn_6.place(x=240, y=260)
        btn_multiply.place(x=340, y=260)
        
        # Btn Row 4
        btn_1.place(x=40, y=330)
        btn_2.place(x=140, y=330)
        btn_3.place(x=240, y=330)
        btn_subtract.place(x=340, y=330)
        
        # Btn Row 5
        btn_0.place(x=40, y=400)
        btn_equal.place(x=240, y=400)
        btn_addition.place(x=340, y=400)
    
    # Calculator Function
    def clear(self):
        # Temporarily disable validation
        self.ent_num_field.config(validate="none")
        # Delete Chars int Ent Field
        self.ent_num_field.delete(0, tk.END)
        # Re-enable validation
        self.ent_num_field.config(validate="key", validatecommand=(self.ent_num_field.register(lambda char: char.isdigit() or char == "" or char in "-+÷%.x(()"), "%S"))    
    
    
    def delete(self):
        expression = self.ent_num_field.get()
        back = expression[:-1]
        self.clear()
        self.ent_num_field.insert(0, back)
        
    def calculate(self):
        expression = self.ent_num_field.get()
        
        expression = expression.replace("÷", "/")
        expression = expression.replace("x", "*")
        
        expression = re.sub(r'(\d+)(\()', r'\1*\2', expression)
        expression = re.sub(r'(\))(\d+)', r'\1*\2', expression)
        
        try:
            if expression != "":
                result = eval(expression)
                self.clear()
                self.ent_num_field.insert(tk.END, result)
        
        except ZeroDivisionError:
            messagebox.showerror('Error', "Division by zero is not allowed.")
        except SyntaxError:
            messagebox.showerror('Error', "Invalid Syntax")
            
    def back_to_main(self):
        self.win.destroy()   
        
        