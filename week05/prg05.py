#2116277 송은화

def gcd(a,b):
    if a < b :
        a, b = b, a # a=큰 값, b=작은 값
    while b != 0 :
        n = a%b
        if n == 0:
            break
        else :
            a=b
            b=n
    return b
print("최대공약수는 %d" %gcd(20,72))
