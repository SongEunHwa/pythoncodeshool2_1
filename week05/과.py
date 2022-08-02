#2116277 송은화
def factorial(i):
    sum = 1
    for a in range(1,i+1):
        sum *= a
    return sum

print(factorial(5))