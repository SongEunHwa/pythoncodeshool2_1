
def factorial(k) :
    Hap = 1
    for i in range(1,k+1):
        if k == 0 :
            return 1
        elif k == 1 :
            return 1
        else:
            Hap *= i
    return Hap

def euler(n) :
    hap = 0
    for i in range(0,n):
        if n < 0 :
            return hap
        else:
            hap += 1/factorial(n)
print(factorial(0))
print(1/factorial(5))
print(euler(5))