import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("./data/countries.csv")
print(df)
df["density"]=df['population']/df['area'] #열추가 - 밀도=인구수/면적

df.drop(index=1,axis=0,inplace=True)
print(df)
df.drop(['capital'],axis=1, inplace = True)
print(df)

ax = plt.gca()
df.plot(kind='bar',x='code',y='area',color='red',ax=ax)
df.plot(kind='line',x='code',y='population',color='blue',ax=ax)
plt.show()
#print(df)