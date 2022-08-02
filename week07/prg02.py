# 2115623 윤주현

def func_mul(x) :
    return x*3

data = [1, 2, 3, 4, 5]
data2 = [10, 20, 30, 40]
print(func_mul(data))
print(data*3)
print(data+data2)
print(list((map(func_mul, data))))
