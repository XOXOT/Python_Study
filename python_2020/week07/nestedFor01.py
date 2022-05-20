#1418083 최희태 : for문
for i in range(5):
    print(i, end=' ')

#중첩된 for문 i:outer 제어변수, j:inner 제어변수
for i in range(3): #outer 제어변수
    for j in range(4): #inner 제어변수
        print("i=%d , j=%d" %(i,j))