import pandas as pd
import matplotlib.pyplot as plt
busan = pd.read_csv('./data/busanIndex.csv')
#print(busan['index'])
print(busan[['economic','heath', 'index']].corr()) # 포릴레이션(관계)을 보여줌 index와의 가장 선형관계는 econmic.

plt.scatter(busan['economic'],busan['index'],color='blue')
plt.show()