import numpy as np
import matplotlib.pyplot as plt
h = np.random.normal(175,10,1000)
plt.hist(h)
plt.show()
#h = 175+10*np.random.randn(1000)
print(np.mean(h))
print(np.std(h))
