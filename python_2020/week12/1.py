tt = ((30,40,30,15),(40,60,80),(90,86,75,40))

list1 = list()
list2 = list()
for i in range(0,len(tt)):
    list1 = list(tt[i])
    list2.append(list1)
print(list2)
list2[1].append(100)
print(list2)