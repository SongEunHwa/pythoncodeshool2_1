## 2116277 ???
import numpy as np
import matplotlib.pyplot as p

h = np.array([1.83,1.76,1.69,1.86,1.77,1.73])
w = np.array([86,74,59,95,80,68])
bmi = w/h**2
print(bmi)
p.boxplot(bmi)
p.show()
print(h)
