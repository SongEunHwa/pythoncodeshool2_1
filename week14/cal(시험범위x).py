#2116277 송은화
from tkinter import *
w = Tk() #윈도우즈 객체 생성
w.title("My Calculator")
display = Entry(w, width=33, bg="yellow") #Entry 입력
display.grid(row=0, column=0, columnspan=5)
button_list = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', ' ',
    '1', '2', '3', '-', ' ',
    '0', '.', '=', '+', ' ',
]
def click(key) :
    if key=="=" :
        r = eval(display.get()) #eval()산술식을 계산해서 함수값으로 변환해줌
        s = str(r)
        display.insert(END,"="+s)
    elif key=="C" :
        display.delete(0,END)
    else :
        display.insert(END,key)  #삽입을 맨끝으로 한다는 뜻

row_index=1
col_index=0
for btn_text in button_list :
    Button(w, text=btn_text, width=5, command=lambda key=btn_text : click(key)).grid(row=row_index,column=col_index)
    col_index += 1
    if col_index >= 5:
        col_index = 0
        row_index += 1
w.mainloop()