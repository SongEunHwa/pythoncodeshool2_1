from tkinter import *
from tkinter import messagebox

def clickLeft(event) :
    d=Tk()

w = Tk()
w.bind("<Button-1>",clickLeft)
w.mainloop()