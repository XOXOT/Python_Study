##컴프리헨션 - 시험출제
#리스트 = 수식 for 항목 in range() if 조건식

mylist=[]
for num in range(1,6):
    mylist.append(num)
print(mylist)   #원래 반복문을 이용한 리스트 출력을
#컴프리헨션을 이용하여 이렇게 표현가능
mylist = [num for num in range(1,6)]
print(mylist) # 이렇게 한줄로 표현가능

mylist = [num*num for num in range(1,6)] #1에서 5까지의 제곱으로 구성된 리스트 출력
print(mylist)

mylist = [num for num in range(1,100) if num%7==0] ##리스트
print(mylist)

mylist = tuple([num for num in range(1,100) if num%7==0]) ##리스트를 튜블로 변형 즉 튜플
print(mylist)

mylist = set([num for num in range(1,100) if num%7==0]) ##리스트를 set으로 변경, 셋은 순차척이 아니다.
print(mylist)