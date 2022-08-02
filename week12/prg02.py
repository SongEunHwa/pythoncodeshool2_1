#1) 필요없는 열 지우기(PassengerId,Name,Ticket
#2) 피벗테이블 ['Sex','Pclass']로
#3)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('./data/titanic.csv')
df.drop(['PassengerId','Name','Ticket'],axis=1,inplace=True)
print(df.info())
table = df.pivot_table(df,['Sex','Pclass'],aggfunc={'Survived':np.sum})
#table.plot(kind='bar',color='red')
#plt.show()
