#리스트 원소의 행의 합과 평균 구하는 프로그램을 작성 (주석
aa = [
    [3,50,20],
    [90,30,70,90,10],
    [60,20,40,20]
]
s =[0,0,0] #행의 합을 구하는 리스트


for i in range(len(aa)):
    total = 0
    for j in range(len(aa[i])):
        total += aa[i][j]
    s.append(total)
print(s)



