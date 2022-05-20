###2에서 100까지 소수를 출력하는 프로그램을 작성

#중첩 for문
for i in range(2,101):
    is_prime = True
    for j in range(2,i):
        if i%j == 0:
            is_prime = False
            break
    if is_prime == True:
        print(i,end=' ')
print()

#중첩 while문