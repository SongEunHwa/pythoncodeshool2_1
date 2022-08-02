import numpy as np
players = np.zeros((100,3))
players[:,0] = np.random.normal(175,10,100)
players[:,1] = np.random.normal(70,10,100)
players[:,2] = np.int64(np.random.normal(24,10,100))
#print(players)

print(np.mean(players, axis=0))
print(np.std(players, axis=0))
print("상관계수=",np.corrcoef(players[:,0],players[:,1]))
