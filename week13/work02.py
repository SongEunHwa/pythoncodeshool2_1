from tkinter import *
import numpy as np

def grade():
    score1 = int(num1.get())
    score2 = int(num2.get())
    avg = (score1+score2)/2
    if avg >= 60 :
        lblResult.configure(text=str(avg)+"합격입니다")
        #label3 = Label(w,text="평균:%2d 합격입니다" %m,fg='red')
        #label3.grid(row=3,column=0,columnspan=2)
    else :
        lblResult.configure(text=str(avg)+"불합격입니다")
        #label3 = Label(w,text="평균:%2d 불합격입니다" %m,fg='red')
        #label3.grid(row=3,column=0,columnspan=2)
w=Tk()
w.geometry("250x100")
label1 = Label(w,text="프로그래밍언어")
label1.grid(column=0,row=0)
num1 = Entry(w,width=20)
num1.grid(column=1,row=0)
label2 = Label(w,text="서비스기획")
label2.grid(column=0,row=1)
num2 = Entry(w,width=20)
num2.grid(column=1,row=1)
button = Button(w,text="계산",command=grade)
button.grid(column=0,row=2,columnspan=2)
lblResult = Label(w,text=" ", fg="red")
lblResult.grid(row=3, column=0, columnspan=2)

w.mainloop()