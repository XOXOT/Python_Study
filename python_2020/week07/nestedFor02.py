#1418083 최희태 2~5단까지 구구단 프로그램
## outer 제어변수 : i, inner 제어변수 : j


for i in range(2,20):
    print("--- %d 단 ---" % i)
    for j in range(2,10):
        print("%d * %d = %d" %(i,j,i*j))
    print()
