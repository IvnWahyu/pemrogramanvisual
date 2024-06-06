from tkinter import *
from tkinter.ttk import *
from plotdata import regression_plot
from stats import stats_columns
import os

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
    
    def create_widgets(self):
        self.winfo_toplevel().title("Data View")
        self.l1 = Label(self.master, text="File Name")
        self.l2 = Label(self.master, text="X Label")
        self.l3 = Label(self.master, text="Y Label")
        
        self.l1.grid(row=0)
        self.l2.grid(row=1)
        self.l3.grid(row=2)
        
        self.eFname = Entry(self.master, width=40)
        self.eX = Entry(self.master, width=40)
        self.eY = Entry(self.master, width=40)
        
        self.eFname.grid(row=0, column=1, sticky=W)
        self.eX.grid(row=1, column=1, sticky=W)
        self.eY.grid(row=2, column=1, sticky=W)
        
        self.txtX = Text(self.master, width=30, height=10)
        self.txtY = Text(self.master, width=30, height=10)
        
        self.txtX.grid(row=3, column=0, sticky=W)
        self.txtY.grid(row=3, column=1, sticky=W)
        
        self.style = Style()
        self.style.map('D.TButton',
                       foreground=[('pressed', 'red'), ('active', 'green')],
                       background=[('pressed', '!disabled', 'black'), ('active', 'white')]
                       )
        
        self.btn = Button(self.master, text="Show Regression Graph", 
                          style="D.TButton", command=self.show_graph)
        self.btn.grid(row=4, column=0, sticky=W)
        
        self.stats = Button(self.master, text="Show Stats", 
                            style="D.TButton", command=self.show_stats)
        self.stats.grid(row=4, column=1, sticky=W)
        
        self.quit = Button(self.master, text="Quit", 
                           style="D.TButton", command=self.master.destroy)
        self.quit.grid(row=4, column=0, sticky=E)
        
    def show_graph(self):
        print(f"File Name: {self.eFname.get()}, X Label: {self.eX.get()}, Y Label: {self.eY.get()}")
        regression_plot(self.eFname.get(), self.eX.get(), self.eY.get())
        
    def show_stats(self):
        print(f"File Name: {self.eFname.get()}, X Label: {self.eX.get()}, Y Label: {self.eY.get()}")
        
        filename = self.eFname.get()
        x_label = self.eX.get()
        y_label = self.eY.get()
        
        # Debugging: Print the full file path
        full_path = os.path.abspath(filename)
        print(f"Trying to open file: {full_path}")
        
        xstats, ystats = stats_columns(filename, x_label, y_label)
        
        print(f"X Stats: {xstats}, Y Stats: {ystats}")
        self.txtX.delete("1.0", END)
        self.txtY.delete("1.0", END)
        self.txtX.insert(INSERT, xstats)
        self.txtY.insert(INSERT, ystats)
        
root = Tk()
app = Application(master=root)
app.mainloop()
