# 2115623 윤주현
# 람다함수 한 줄로 함수를 간단히 정의해주는 것
mul = lambda n1, n2 : n1*n2
print(mul(20, 2))

avg = lambda n : sum(n)/len(n)
print("평균 =", avg([50, 30, 25, 45, 55]))
