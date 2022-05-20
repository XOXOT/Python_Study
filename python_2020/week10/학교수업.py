###1418083 최희태

aa = [10,20,30,40]
print(aa[-1])
print(aa[0])
#print(aa[len(aa)])
print(aa[1:3])

mylist=[5,2,2,5]
h=0
for i in range(0, len(mylist)):
    h+=mylist[i]
    print("결과==>%d"%h)

#소수 구하기
list1 = list()
for num in range(2,10):
    is_prime = True
    for i in range(2,num):
        if num % i ==0:
            is_prime=False
            break
    if is_prime:
        list1.append(num)
    print(list1)


##2번 문제
values = [30,40,70,80,23,65,78]
iMin = values[0]
for num in values:
    if iMin > num:
        iMin = num
print("최솟값=",iMin)

values = [30,40,70,80,23,65,78]
iMax = values[0]
for num in values:
    if iMax < num:
        iMax = num
print("최대값=",iMax)

##과제

##문제2 최소값과 최대값을 계산하고, 범위(range는 최대값-최소값)를 구하는 프로그램을 작성

score = [70,56,89,100,60,80,65,88]
Max = score[0]
for i in values:
    if Max < i:
        Max = i
print("최대값=",Max)

Min = score[0]
for i in values:
    if Min > i:
        Min = i
print("최솟값=",Min)

print("범위 %d" %(Max-Min))