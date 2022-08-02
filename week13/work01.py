from tkinter import *
from tkinter import messagebox
def grade():
    score = int(num1.get())
    if score >= 60 :
        messagebox.showinfo("",str(score)+"점은 합격입니다")
    else :
        messagebox.showinfo("","%d점은 불합격입니다"%score)
w=Tk()
w.geometry("200x50")
label = Label(w,text="점수입력",font=('궁서체',8))
label.grid(column=0,row=0)
num1 = Entry(w,width=20)
num1.grid(column=1,row=0)
button = Button(w,text="계산",command=grade)
button.grid(column=0,row=1,columnspan=2)
w.mainloop()