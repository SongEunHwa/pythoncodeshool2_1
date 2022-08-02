##2116277 송은화
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
import numpy as np
font_path= "C:\Windows\Fonts\malgun.ttf"
f_name=font_manager.FontProperties(fname=font_path,size=15)
font1= font_manager.FontProperties(fname=font_path).get_name()
rc("font",family=font1)

df = pd.read_csv("./data/busanIndex.csv",encoding='utf-8')
print(df.info())
#가장 큰 사회안전지수 값
print("사회안전지수가 가장 큰 값=",df["index"].max())
#경제활동분야와 건강보건의 상관계수
print("상관계수=",np.corrcoef(df["economic"],df["heath"]))

df.plot(x='SIG_KOR_NM',y='index')
plt.title("부산시 구군별 사회안전지수")
plt.xlabel("부산의 자치구")
plt.ylabel("사회안전지수")
plt.show()