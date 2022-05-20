###1418083 최희태

bb = (2,2,4,5,5)

aa =[[10,20,30,40],[23,17,78],[79,20,100,120]]
print(aa[0][1])
print(aa[1])
print(len(aa[2]))

tt = ((30,40,30,15),(40,60,80),(90,86,75,40))

for i in range(0,len(tt)):
    for j in range(0,len(tt[i])):
        print(tt[i][j],end =" ")
    print()

list1 = list(tt)
print(list1)

list1 = list()
list2 = list()
for i in range(0,len(tt)):
    list1 = list(tt[i])
    list2.append(list1)
print(list2)

list2[1].append(100)
print(list2)

for i in range(0,len(list2)):
    list2[i].remove(40)
print("40삭제",list2)
