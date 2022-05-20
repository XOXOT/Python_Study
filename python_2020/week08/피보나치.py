###for문
num1, num2, num3 = 1, 1, 0
print(num1,num2,end = " ")
for i in range(1, 51):
    num3 = num1 +num2
    if num3 >100:
        break
    print(num3, end=" ")
    num1 = num2
    num2 = num3
print()
print("------------------------------------------------------------------------------------------")
### while문
num1, num2, num3 = 1, 1, 0
while num1 <= 100:
    num3 = num1 +num2 #num1과  num2를 더하여 더움에 더할 수를 만둘어 놓음
    print(num1, end= ' ') #각 항 출력 num1부터 넣어야 1이 두번 나옴
    num1 = num2 #2번째 항이었던 것을 1번째 항으로 전환
    num2 = num3 #다음 항을 두번째 항으로 전환하여 반복
print() #num1=1 num2=1,num3=2/ num1=1 num2=2 num=3/ num1=2 num2=3 num3=5
print("------------------------------------------------------------------------------------------")
### while문 2
a, b = 0,1
while b <100:
    print(b, end=' ')
    a,b=b,a+b #왼쪽부터 오른쪽으로 순서대로 계산 후 왼쪽 변수에 대입
print()
print("------------------------------------------------------------------------------------------")
#최종 while문

num1, num2, num3 = 1, 1, 0
print(num1, " ", num2, end=" ")
i = 1
while i < 51:
    num3 = num1 + num2 #num1과  num2를 더하여 다움에 더할 수를 만둘어 놓음
    if num3 > 100 :
        break #만약 num3이 100보다 커지면 break해라
    print(num3, end=" ")
    num1 = num2 #2번째 항이었던 것을 1번째 항으로 전환
    num2 = num3 #다음 항을 두번째 항으로 전환하여 반복