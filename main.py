import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog

class myApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x600+0+0")
        self.title("Pera ko")
        self.resizable(False, False)

        self.mainFrame()
        self.createMenu()

    def mainFrame(self):
        #Top frame widgets
        lbl_title = tk.Label(self, bd=20, relief=tk.FLAT, text="Date here", fg="blue", bg="linen",
                             font=("times new roman", 20, "bold"))
        lbl_title.pack(side=tk.TOP, fill=tk.X)
        
        mainFrame = tk.Frame(self, bd=20, relief=tk.FLAT)
        mainFrame.place(x=0, y=75, width=500, height=525)
        
        
        btn_search = tk.Button(self, text="⌕",font=("arial", 20), fg="white", bg="green", command=self.search)
        btn_search.place(x=450, y=20, width=30, height=30)

        #Button on the left side of date 
        btn_date_left = tk.Button(self, text="<",font=("arial", 10), fg="black", bg="white", command=self.search)
        btn_date_left.place(x=140, y=20, width=30, height=30)
        
        #Button on the right side of date 
        btn_date_right = tk.Button(self, text=">", font=("arial", 10), fg="black", bg="white", command=self.search)
        btn_date_right.place(x=330, y=20, width=30, height=30)

    def createMenu(self):
        menubar = tk.Menu(self)
        
        # Create a submenu for file_menu
        file_menu = tk.Menu(menubar, tearoff=0)
        
        # Add a command directly to the menubar
        menubar.add_command(label="Export records", command=self.export_records)
        menubar.add_command(label="Backup & restore", command=self.backup_records)
        menubar.add_command(label="Delete & Reset", command=self.delete_record)
        menubar.add_command(label="About", command=self.about)
        
        # Configure the menubar
        self.config(menu=menubar)
    
    def search(self):
        # Implement your export logic here
        pass
        
    def export_records(self):
        # Implement your export logic here
        pass
    
    def backup_records(self):
        # Implement your backup logic here
        pass

    def delete_record(self):
        # Implement your delete logic here
        pass
    
    def about(self):
        messagebox.showinfo("About", "Pera ko\nv1.0\nDeveloped by:\nChristianJude23 & owenlim225")

app = myApp()
app.mainloop()
