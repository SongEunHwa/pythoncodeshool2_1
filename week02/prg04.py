## if문에 관한 문제(2116277 송은화)

num = int(input("점수=>"))
grade = ""
if num >= 90 :
    grade = "A"
elif num >= 80 :
    grade = "B"
elif num >= 70:
    grade ="C"
else :
    grade = "F"

print("당신의 점수 %d, 학점은 %c" %(num,grade))