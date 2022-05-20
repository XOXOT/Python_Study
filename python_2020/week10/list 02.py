## 2차원 리스트
list1= [[2,3,5,9],[2,4,13,43],[2,12,32,5]]
print(list1[2])
aa= [[3,2,5,7],[18,14,15,17],[21,25,22,27]]
print(aa)
print(aa[0])
print(aa[1][1])

###for문을 이용한 리스트 생성
a=list() #1차원 리스트
aa=list() #2차원 리스트
value = 0
for r in range(3):
    for c in range(3):
        value +=1
        a.append(value) #r=0 c=0 value =1 / r=1 c=1 value=2 / r=2 c=2 value =3 stop  #value값을 a리스트에 추가
    aa.append(a) # aa에 리스트 a 추가
    a=[] #a초기화
print(aa)
print(aa[0])
print(aa[1][1])


##2차원 리스트 하나하나 출력
for r in range(3):
    for c in range(3):
        print(aa[r][c], end= ' ')
    print()

