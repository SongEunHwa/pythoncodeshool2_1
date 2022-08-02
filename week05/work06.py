#2116277 송은화
myShop={"옷":100,"컴퓨터":2000,"모니터":320}
print(myShop["컴퓨터"])
print(myShop.get("옷"))
myShop["폰"] = 400
print(myShop)
print(list(myShop.keys()))
print(sum(myShop.values()))
#딕셔너리 출력
for key in myShop.keys():
    print("%s -> %d" %(key,myShop.get(key)))


               