### append 함수
n_list = list()
n_list.append(20)
n_list.append(35)
n_list.append(45)
n_list.append(70)
print(n_list)

###insert 함수
n_list.insert(1,100)
print(n_list)

##오름차순 정렬
n_list.sort()
print(n_list)

##내림차순 정렬
n_list.reverse()
print(n_list)

##원소의 개수 알려주는 함수
print(len(n_list))

##삭제 유형 1 인덱스 삭제
del(n_list[1])
print(n_list)

##삭제 유형 2 값을 삭제
n_list.remove(100)
print(n_list)

##값의 인덱스를 알려주는 함수
print(n_list.index(20))

##합,최대,최소
n_list.append(75)
n_list.append(85)
print(n_list)
print(sum(n_list))
print("평균 %f" %(sum(n_list)/len(n_list)))
print("범위 %d" %(max(n_list)-min(n_list)))
