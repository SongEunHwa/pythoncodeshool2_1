from tkinter import *
from tkinter import messagebox
def box() :
    messagebox.showinfo("Hi~~~","안녕하세요")

w = Tk()
w.title('2116277 송은화')
w.geometry("300x200")
w.resizable(width=False,height=False)
button = Button(w,text="확인",command=box)
button.pack()
w.mainloop()