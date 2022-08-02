## 2116277 송은화(확장형 데이터)

a = [[10,20,30],
     [40,50,60],
     [70,80,90]]
for val in a :
    print(val)

for row in range(len(a)):
    for col in range(len(a[row])):
        print(a[row][col], end=' ')
    print()

