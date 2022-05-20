###???
tt1=(70,80,80,30)
tt=((30,40,3,15),
    (40,60,80),
    (90,86,75,40))

for i in range(0,len(tt)):
    for j in range(0,len(tt[i])):
        print(tt[i][j],end=" ")
    print()

###1418083 최희태
###dictionary
student1 = {'학번' : 1000, '이름': '홍길동', '학과': '경영정보학과'}
student2 = {'학번' : 2000, '이름': '이순신', '학과': '경영학과','학번':400000}
print(student1)
print(student1['이름'])
print(student1.get('이름'))
student1['tel'] = '010-5550-1234'  ###dic에 추가하는 법
print(student1)
student1['이름'] = '성춘향' ###원래있던거 덮어쓰기(수정)
print(student1)
del(student1['tel'])
print(student1) ###삭제
print(student2)  ###뒤에 또 학번을 적으면 뒤에 있는 것으로 수정해서 출력된다.
print(student1.keys())  ###dic의 key를 list로 출력
print(student1.values()) ###dic의 values을 list로 출력

