from tkinter import *
from tkinter import messagebox

def calBmi() :
    bmi = float(eWeight.get())/ float(eHeight.get())**2 #bmi계산
    #label1['text'] = bmi
    messagebox.showinfo("당신의 bmi지수",bmi)
w = Tk()
w.title("2116277 송은화 (BMI 프로그램)") #창의제목표시
w.geometry("250x300") #창의크기
label1 = Label(w,text="몸무게(Kg)",fg="blue") #레이블 위젯을 생성
eWeight = Entry(w,text="",fg="red") #한줄 텍스트 입력
label2 = Label(w, text="신장(m)",fg='blue')
eHeight = Entry(w, text="")

btnOk = Button(w, text="확인",command=calBmi)
label1.grid(row=0, column=0) #레이블을 창에 배치
eWeight.grid(row=0, column=1)
label2.grid(row=1, column=0)
eHeight.grid(row=1, column=1)
btnOk.grid(row=2, column=0,columnspan=2)
w.mainloop()  #사용자 이벤트를 대기
