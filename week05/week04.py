## 2116277 송은화 #
matrix = [[10,20,30],
          [40,50,60],
          [70,80,90]]
t_matrix= [[0,0,0],
           [0,0,0],
           [0,0,0]]

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        t_matrix[col][row] = matrix[row][col] #행과 열을 바꿈

print("원본행렬=",matrix)
print("전치행렬=",t_matrix)


t1=[]
for i in range(len(matrix)) : #i=0,1,2
    t_row = []
    for row in matrix :
        t_row.append(row[i])
    t1.append(t_row)
print("전치행렬2",t1)
