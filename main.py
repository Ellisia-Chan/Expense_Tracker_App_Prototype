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
        
        #Export records
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Export records", command=self.export_record)
        file_menu.add_command(label="Backup & restore", command=self.backup_record)
        menubar.add_cascade(label="Delete & Reset", menu=self.delete_record)
        
        self.config(menu=menubar)
        
        
    #CHRISTIAN IKAW NA BAHALA
    def export_records(self):
        pass
    
    def backup_records(self):
        pass

    def delete_record(self):
        pass
    

app = myApp()
app.mainloop()
