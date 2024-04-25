from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("400x400")

# Program 1
program1_label = Label(top, text="Program 1")
program1_label.pack()

def helloCallBack():
   msg = messagebox.showinfo("Hello Python", "Hello World")

B = Button(top, text="Hello", command=helloCallBack)
B.pack()

# Program 2
program2_label = Label(top, text="Program 2")
program2_label.pack()

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text="Music", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=20)
C2 = Checkbutton(top, text="Video", variable=CheckVar2, onvalue=1, offvalue=0, height=5, width=20)
C1.pack()
C2.pack()

# Program 3
program3_label = Label(top, text="Program 3")
program3_label.pack()

L1 = Label(top, text="User Name")
L1.pack()
E1 = Entry(top, bd=5)
E1.pack()

# Program 4
program4_label = Label(top, text="Program 4")
program4_label.pack()

frame = Frame(top)
frame.pack()

bottomframe = Frame(top)
bottomframe.pack()

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack()

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack()

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack()

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack()

# Program 5
program5_label = Label(top, text="Program 5")
program5_label.pack()

var = StringVar()
label = Label(top, textvariable=var, relief=RAISED)
var.set("Hey!? How are you doing?")
label.pack()

# Program 6
program6_label = Label(top, text="Program 6")
program6_label.pack()

Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.pack()

# Program 7
program7_label = Label(top, text="Program 7")
program7_label.pack()

mb = Menubutton(top, text="condiments", relief=RAISED)
mb.pack()
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu

mayoVar = IntVar()
ketchVar = IntVar()
mb.menu.add_checkbutton(label="mayo", variable=mayoVar)
mb.menu.add_checkbutton(label="ketchup", variable=ketchVar)

# Program 8
program8_label = Label(top, text="Program 8")
program8_label.pack()

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

# Program 9
program9_label = Label(top, text="Program 9")
program9_label.pack()

var = StringVar()
label = Message(top, textvariable=var, relief=RAISED)
var.set("Hey!? How are you doing?")
label.pack()

# Program 10
program9_label = Label(top, text="Program 10")
program9_label.pack()

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=sel)
R1.pack( anchor = W )
R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=sel)
R2.pack( anchor = W )
R3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=sel)
R3.pack( anchor = W)
label = Label(root)
label.pack()

top.mainloop()