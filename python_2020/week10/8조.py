##프로그래밍 02분반 8조 10주차 조별과제 최희태
score=[70,56,89,100,60,80,65,88] #score에 리스트 형식
sum=0 #변수의 초깃값을 설정해줌
for i in score: #i에 score의 원소를 하나씩 넣음
    sum+=i #sum에는 i를 더한 값을 다시 할당
print("점수 총합:",sum) #score의 원소값이 하나씩 더해진 sum을 출력함

score=[70,56,89,100,60,80,65,88] #score에 리스트 형식
sum=0 #변수의 초깃값을 설정해줌
for i in score: #i에 score의 원소를 하나씩 넣음
    sum+=i #sum에는 i를 더한 값을 다시 할당
print("점수 평균:", sum/len(score)) #평균는 숫자의 합을 전체의 갯수로 나눈 값이라서 총합을 len()함수를 통해 나눠서 평균값 출력

score = [70,56,89,100,60,80,65,88]

print("합 %d" % sum(score))
print("평균 %f" %(sum(score)/len(score)))

score=[70,56,89,100,60,80,65,88] #score에 리스트 형식
mean = sum(score)/len(score) #평균값
vsum = 0 #변수의 초깃값을 설정해줌
for i in score: #i에 score의 원소를 하나씩 넣음
    vsum = vsum + (i-mean)**2 #편차는 변량-평균, 분산은 편차 제곱의 평균값으로 먼저 편차의 제곱의 합을 구함
var = vsum / len(score) #편차의 제곱의 합을 len()함수를 통해 나눔
print("점수 분산:",var) #분산값 출력

##2
score=[70,56,89,100,60,80,65,88] #최댓값 구하기
iMax = 0 #초깃값 설정
for num in score: #num에 score의 원소를 하나씩 넣음
    if iMax < num: #숫자를 계속 비교해서 큰 숫자를 iMax로 바꿈
        iMax = num
print("최댓값=", iMax) #최댓값을 출력

score=[70,56,89,100,60,80,65,88] #최솟값 구하기
iMin = score[0] #score의 첫번째 원소를 변수 iMin에 저장함
for num in score: #num에 score의 원소를 하나씩 넣음
    if iMin > num: #숫자를 계속 비교해서 작은 숫자를 iMin를 바꿈
        iMin = num
print("최솟값=", iMin) #최솟값을 출력

print("최댓값-최솟값=>%d" % (iMax-iMin)) #최댓값에서 최솟값을 뺀 범위 출력