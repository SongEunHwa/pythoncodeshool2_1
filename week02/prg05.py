## 1. 연산자에 관한 문제(2116277,송은화)

num1=int(input("두 자리 숫자1 입력 =>"))
num2=int(input("두 자리 숫자2 입력 =>"))
print("%d + %d = 10%d" %(num1,num2,num1+num2))
print("%d * %d = 10%d" %(num1,num2,num1*num2))
print("%d // %d = 10%d" %(num1,num2,num1//num2))
print("%d > %d는 %s" %(num1,num2,num1>num2))
print("%d <= %d는 %s" %(num1,num2,num1<=num2))
print(num1 > num2 and num1 <= num2)
print(num1 > num2 or num1 <= num2)