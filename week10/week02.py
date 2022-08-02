import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
f_path= "C:\Windows\Fonts\malgun.ttf"
f_name=font_manager.FontProperties(fname=f_path,size=20)
f1= font_manager.FontProperties(fname=f_path).get_name()
rc("font",family=f1)
x = ['Mon',"Tue","Wed","Thur","Fri","Sat","Sun"]
y1 = [15.6,14.2, 16.3, 18.2, 17.1, 20.2, 22.4]
y2 = [20.1, 23.1, 23.8, 25.9, 23.4, 25.1, 26.30]
plt.title("Temperature of Cits(서울&부산)",fontproperties=f_name)
plt.plot(x,y1,label="서울")
plt.plot(x,y2,label="부산")
plt.xlabel("day")
plt.ylabel("기온(섭씨)")
plt.legend()
plt.show()