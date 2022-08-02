import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/countries.csv")
#print(df.info())
#print(df.describe())
df['density'] = df['population']/df['area']     #week11.2.(4)
aa = df[3:6,2]
print(aa)
#print(df)

data1 = df[df['density']>=300]  #week11.2.(5)
#print(data1)

gdp1 = [32115,65717,41491,9979,11287]   #week11.2.(6)
df['gdp1']=gdp1
#print(df)

df.plot(kind='bar',x='country',y='gdp1',color='blue')  #week11.2.(7)
#plt.show()

