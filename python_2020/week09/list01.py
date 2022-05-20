aa = [70,80,100,45,70,66,80,90,75,68,99] #리스트에 값 선언
#print(aa[1]) #리스트 원소 출력
#hap = aa[0] + aa[1] + aa[2]+ aa[3]+ aa[4]+ aa[5]
hap = 0
for i in range(len(aa)): #리스트의 크기를 알 수 있는 함수 len함수
    hap+= aa[i]
print("합 = %d, 평균 = %f" %(hap, hap/len(aa)))

n_list = [11,22,33,44,55,66]
n_list[2:4] #[33,44]
del(n_list[2])
n_list#[11,22,44,55,66]
n_list[2:3] = [33]
n_list#[11,22,33,55,66]

n_list[2:4]=[33,44]
n_list # [11,22,33,44,66]

n_list.remove(44)
n_list #[11,22,33,66]

44 in n_list #False
66 in n_list #True
