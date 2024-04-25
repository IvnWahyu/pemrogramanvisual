import tkinter as tk
from tkinter import *


root = tk.Tk()

Frameku = tk.Frame(root, bg = 'blue')
Frameku.place(relwidth = 1, relheight = 1)

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = tk.Checkbutton(Frameku, text = "Music", variable = CheckVar1, \
   onvalue = 1, offvalue = 0, height=5, \
   width = 20, )
C2 = tk.Checkbutton(Frameku, text = "Video", variable = CheckVar2, \
   onvalue = 1, offvalue = 0, height=5, \
   width = 20)
C1.pack()
C2.pack()
root.mainloop()