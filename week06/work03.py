## 2116277 송은화
#from turtle import *  사용시에 바로 forward
import turtle as t
def draw_circle(n):
    m = 360/n
    for i in range(n):
        t.circle(100)
        t.left(m)

def draw_square(size):
    for i in range(4):
        t.fd(size) #fd=forward
        t.left(90)
        size += 5

def draw_line():
    t.fd(100)
    t.backward(100)

t.color('red')

for i in range(20):
    draw_line()
    t.left(360/20)


draw_circle(12)
#for i in range(10,200,20): #한바퀴도는게 20  #draw_square에 관한 for문
#    draw_square(i)
#draw_square(10)
t.done() #창이 사라지지 않음

