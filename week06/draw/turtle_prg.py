#2116277 송은화
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

