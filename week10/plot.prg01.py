#from matplotlib import pyloot as plt
import matplotlib.pyplot as plt
## 한글 폰트 설정하기
import matplotlib.font_manager as fm
f_path='C:\Windows\Fonts\malgun.ttf' #원하는 폰트를 f_path로 대입
font = fm.FontProperties(fname=f_path,size=18)
x=['2000','2005','2010','2015','2019']
ko = [11030,18520,22290,28720,33720]
jp = [36230,40560,43440,38840,41690]
ch = [940,1760,4340,7940,10410]
plt.plot(x, ko,color='red',marker='o',linestyle='solid')
#plt.plot(x,ko,'ro-')
plt.plot(x,jp,'b*--')
plt.plot(x,ch,'g+-.')
plt.title('아시아 1인당 국민소득',fontproperties=font)
plt.xlabel("년도",fontproperties=font)
plt.legend()
plt.ylabel('dollars')
plt.show()