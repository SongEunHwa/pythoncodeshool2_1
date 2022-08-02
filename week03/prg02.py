# 2116277 송은화
temp=[28,31,33,35,27,26,25] #리스트 초기화
hap = 0 ; iMax=temp[0] ; iMin = temp[0]
for data in temp :
    #print(data, end="  ")
    hap += data
    if iMax < data :
        iMax = data
    if iMin > data :
        iMin = data
print("합= %d,최댓값= %d, 최솟값= %d" %(hap,iMax,iMin))
print("평균= %7.2f" %(hap/len(temp)))