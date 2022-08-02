from tkinter import *
from tkinter import messagebox
def fun1():
    ans = messagebox.askyesno("확인","프로그램 종료하시겠습니까?")
    print(ans)
    if ans :
        w.destroy() #창을 닫고, 메모리에서 지워줌
    else:
        w.title("취소하였습니다.")

w = Tk()
w.title("2116277 송은화 (이벤트)")
w.geometry('400x250')
btn= Button(w,text="확인",command=fun1)
btn.pack()

w.mainloop()