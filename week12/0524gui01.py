from tkinter import *
from tkinter import messagebox
def call() :
    print("안녕하세요~ 파이썬 수업 중 입니다~")
    messagebox.showerror("Hi~~~","파이썬 수업을 재미있게 하자!!!")

w = Tk()
w.title("2116277 송은화")
w.geometry("250x300")
btn0k = Button(w, text="확인",command=call) #확인을 누르면 call호출
btn0k.pack()
w.mainloop()
