import tkinter as tk

class myApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x600+0+0")
        self.title("Pera ko")
        self.resizable(False, False)

        self.mainFrame()
        self.createMenu()

    def mainFrame(self):
        lbl_title = tk.Label(self, bd=20, relief=tk.RIDGE, text="<  Date here  >", fg="blue", bg="linen",
                             font=("times new roman", 20, "bold"))
        lbl_title.pack(side=tk.TOP, fill=tk.X)
        
        mainFrame = tk.Frame(self, bd=20, relief=tk.RIDGE)
        mainFrame.place(x=0, y=75, width=500, height=525)

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
    # Implement your delete logic here
        pass

app = myApp()
app.mainloop()
