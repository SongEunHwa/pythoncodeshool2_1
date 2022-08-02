## 2116277 송은화
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
font_path= "C:\Windows\Fonts\malgun.ttf"
f_name=font_manager.FontProperties(fname=font_path,size=15)
font1= font_manager.FontProperties(fname=font_path).get_name()
rc("font",family=font1)
x = ['2015','2016','2017','2018','2019','2020']
y2 = [1694,1744,1683,1677,1703,1651]
y3 = [1248,1300,1224,1244,1223,1204]
y4 = [1507,1598,1560,1581,1584,1561]
plt.title("시도별 취업자수")
plt.plot(x,y2,'*-',label="부산")
plt.plot(x,y3,'o-',label="대구")
plt.plot(x,y4,'+-',label="인천")
plt.xlabel("년도(기준:후반기)")
plt.ylabel("도시(천명)")
plt.legend()
plt.show()