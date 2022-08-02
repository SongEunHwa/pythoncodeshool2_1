a = 0 #euler 값 초기화

def factorial(k) :
    if k == 1 :
        return 1
    elif k == 0 :
        return 1
    else :
        return k * factorial(k-1)

def euler(n) :
    hap = 0
    for i in range(0,n+1) :
        hap += 1/factorial(i)
    return hap

print("euler(%d)=%7.4f" %(5,euler(5)))
print("euler(%d)=%7.4f" %(5,euler(20)))
