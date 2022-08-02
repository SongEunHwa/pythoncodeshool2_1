import pandas as pd

titanic = pd.read_csv("./data/titanic.csv")
adata = titanic.loc[titanic['Age']<20,["Name","Age"]]
#print(adata)

# 성별과 나이의 평균값을 성별로 그룹화하라
#print(titanic[['Age','Sex']].groupby('Sex').mean())
#print(titanic[['Age','Sex','Fare']].groupby('Sex').mean())
#print(titanic.groupby('Sex')[['Age','Fare']].mean())

#각 승객 등급의 수
print(titanic[titanic['Pclass']==1].count())
#print(titanic.sort_values(['Pclass','Age'],ascending=False).head())