## 3.반복문을 이용하여 프로그램 작성(2116277,송은화)
## 시험 점수들을 통해 평균 알아보기
score = 1 ; sum = 0
sum1 =0
subject = []
while True :
    score = int(input("과목을 입력하시오. 없을시 0으로 끝내기 =>"))
    if score == 0 :
        break
    subject.append(score)
    sum1 += score

print("시험점수의 평균 = %5.2f" %(sum1/len(subject)))
