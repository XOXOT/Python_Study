###???
student_tuple=(('20201','홍길동','011-123-4567'), ('20102', '이순신', '010-234-4545'),
               ('20103', '성춘향', '010-345-8987'))
list01=[]
list02=[]
for i in range(3):
    list01.append(student_tuple[i][0])
    list02.append(student_tuple[i][1])
student_dict = dict(zip(list01,list02))
print(student_dict)

###???
oldlist = ['짜장면', '짬뽕', '탕수육']
newlist = [5000,8000,15000]
data = list(zip(oldlist,newlist))
print(data)
a,b = zip(*data)
print(a)
print(b)

### 1418083 최희태
list1 = ['짜장면', '라면', '탕수육']
list2 = [7000,5000,15000]
list3 = ['A', 'A', 'C']
for val in zip(list1,list2, list3):
    print(val)

data = zip(list1, list2, list3)
print(data)  ###주소값만 나온다. 즉 리스트로 형을 변화하여야 한다.

data = list(zip(list1, list2, list3))
print(data)

data = dict(zip(list1, list2))
listdata = list(zip(list1, list2, list3))
print(data) ##딕셔너리로 변환
print(data["라면"]) #라면의 벨류나옴
print(listdata[0][0]) #리스트 인덱스 0(list1)의 인덱스 0을 출력

listA, listB, listC  = zip(*listdata) #언팩하면 튜플 형태로 나오고 원래의 형태가 나옴
print(listA)
print(listB)
print(listC)
