### 1418083 최희태

for i in range(1,6):
    for j in range(1, i+1):#i=1 1,2까지출력 = 1, i=2는 2에서 3까지 =2
        print(j, end="")
    print()

i=1
while i <= 5:
    j=1
    while j<i+1:
        print(j, end="")
        j+=1
    i+=1
    print()



for i in range(10):
    for j in range(i,10):
        print("*", end='')
    print()

i=10
while i>0:
    j=1
    while j < i+1:
        print("*", end='')
        j+=1
    i-=1
    print()

i =10
while i>0: #i가 0이상일때까지 반복.
    print("*"*i) #출력된 i값에 * 곱하기
    i-=1 #출력된 i값에 -1을 하고 while값을 반복한다.

i=10
while i>0:
    print("*"*i)
    i-=1

a=5%3
print(a)