#### 1418083 최희태

n=6
for i in range(n):
    for j in range(i):
        print(' ',end='') #공백 뒤에는 줄바꿈이 없어야함 #공백을 몇개를 찍을 것인가? #n = 6, j=0,1,2,3,4,5
    for j in range(n-i):
        print("*", end='') #별을 몇개를 찍을 것인가?
    print()

print("------------------------------------------------------------------------------------------")

n=6
for i in range(n): #n=6 #i=0,1,2,3,4,5
    for j in range(n-(i+1)): #j=5,4,3,2,1
        print('*',end='')
    for j in range((2*i)+1): #1,3,5,7,9,11
        print(j, end='')
    print()