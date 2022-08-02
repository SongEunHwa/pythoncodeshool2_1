#2116277 송은화
a = int(input("큰 수를 입력 =>"))
b = int(input("작은 수를 입력=>"))

while b != 0 :
    n = a%b
    if n == 0:
        break
    else :
        a=b
        b=n
print("최대공약수는 %d" %b)
