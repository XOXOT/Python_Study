###1418083 최희태

n=6
for i in range(n): #n=6, i=0,1,2,3,4,5
    for j in range(n-(i+1)): # 6-(0+1),6-(1+1)...
        print(' ', end='')
    for j in range(i+1):
        print('@', end='')
    print()

print("------------------------------------------------------------------------------------------")

i = 0
while i < 6: #i가 0,1,2,3,4,5까지 반복
    i+=1 # i값에 +1씩 대입
    print((' ' * (6 - i)) + ('@'*i)) #빈칸을 앞에 두고 총 자릿수인 6에 i값씩 뺌/뺀 빈칸은 i값에 @를 채워넣음 그리고 다시 반복

print("------------------------------------------------------------------------------------------")

n, i = 6,0
while i <n: #아우터 변수 i가 n보다 작을 때까지 반복
    j=0
    while j < (n-(1+i)): # 6-(1+0),6-(1+1)... 빈칸하나는 @으로 채워야하기 때문에 시작숫자 n에서 i에 +1을 함
        print(' ', end='') #즉 n이 6, i는 0 j는 0일때 01234가 빈칸으로 출력됨
        j+=1
    while j <n:
        print('@', end='') #n이 6, i는 0 j는 0일때 나머지 012345중 5가 @로 출력됨
        j+=1
    i+=1 #i에 +1을 한 후에 다시 반복
    print() #그 다음 반복문은 다음 행으로 출력
