###1418083 최희태

for i in range(1,6):
    for j in range(1, i+1): #i=1 1,2까지출력 = 1, i=2는 1에서 3까지 =1,2
        print(j, end="") #j를 출력하는데 줄바꿈으로 출력
    print() #그 다음 반복문은 다음 행으로 출력

print("------------------------------------------------------------------------------------------")

i=1
while i <6:
    j=1
    while j<=i: #j는 i보다 작거나 같을 때까지 출력
        print(j, end="")
        j+=1 #조건이 끝났으면 j에 +1을 하여 다시 반복
    i+=1 #j에 대한 반복이 끝났으면 i에 +1을 하여 다시 전체 반복
    print() #그 다음 반복문은 다음 행으로 출력


print("------------------------------------------------------------------------------------------")

###1418083 최희태

for i in range(10):
    for j in range(i, 10):
        print("*",end ="")
    print()
print("------------------------------------------------------------------------------------------")
i =10
while i>0: #i가 0이상일때까지 반복.
    print("*"*i) #출력된 i값에 * 곱하기
    i-=1 #출력된 i값에 -1을 하고 while값을 반복한다. 
print("------------------------------------------------------------------------------------------")
i=10
while True: #while문을 수행할 때마다 i값을 증가시킨다.
    if i<=0:
        break #i값이 10으로 시작하여 0이될때 while값을 벗어나도록 한다
    print("*"*i) # i값에 *을 곱하라
    i-=1 #출력된 값에 -1을 하고 다시 while값을 반복한다.
print("------------------------------------------------------------------------------------------")
i=10 #i가 10부터 시작
while i>0: #i가 0보다 클때까지 반복
    j=1 #j는 1부터 시작
    while j <=i: #j가 i보다 크거나 작을 떄까지 반복 즉 j가 1이고 i가 10이면 1부터 10까지 반복
        print("*", end='') #j값 프린트를 *로 j였으면 12345678910으로 나오고 end함수에 의하여 줄바꿈
        j+=1 #j값에 +1하여 다시 반복 1일때는 2로
    i-=1 #j에 대한 반복이 끝났으면 다시 i값에 -1후에 다시 반복 10일때는 9로
    print() #그 다음 반복문은 다음 행으로 출력








