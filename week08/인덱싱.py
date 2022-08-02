import numpy as np
data = np.array([[3,5,10],[8,10,12],[7,10,23]])

print(data.sum(axis=0)) #열 [18 25 43]
print(data.sum(axis=1)) #행 [18 30 40]

print(data.std(axis=1))
print(np.std(data[0,]))