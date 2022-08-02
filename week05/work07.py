# 2116277 송은화
# 시험점수를 딕셔너리에 저장, 출력하고 원하는 값찾기

mysore = {"국어":80,"영어":76,"수학":91,"과학":79,"사회":98}
cla = input("알고 싶은 점수의 과목을 입력하시오.").split(",")
for i in cla :
    if i in list(mysore.keys()):
        print(i,"의 점수는",mysore.get(i),"점")
    else :
        print(i,"의 점수는 입력되지 않았습니다.")
