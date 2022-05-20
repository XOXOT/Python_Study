##과제

##문제1 리스트 원소의 합, 평균, 분산을 구하는 프로그램을 작성하라.

score = [70,56,89,100,60,80,65,88]

print("합 %d" % sum(score))
print("평균 %f" %(sum(score)/len(score)))



##문제2 최소값과 최대값을 계산하고, 범위(range는 최대값-최소값)를 구하는 프로그램을 작성

score = [70,56,89,100,60,80,65,88]
Max = score[0]
for num in score:
    if Max < num:
        Max = num
print("최대값=",Max)

Min = score[0]
for num in score:
    if Min > num:
        Min = num
print("최솟값=",Min)

print("범위 %d" %(Max-Min))