###중첩 for문 소수
primes = [] #리스트 생성

for num in range(2, 101) : #2부터 100까지
    is_prime=True #소수인 경우
    for j in range(2,num): # 2부터 시작하고 n+1이 아닌 이유는 소수의 특성상 약수의 개수가 2가 되는게 1과 n밖에 없으므로 1과 n을 제외(n-1)하여 시작.
        if num % j == 0 : # 앞에서 제외를 했으므로 0으로 나누어 떨어지는게 만족을 해버리면 소수가 아니라는 뜻
            is_prime = False #소수가 이닌 경우

    if is_prime: #is prime이 True라면 그 값은 소수이고
        primes.append(num) #primes리스트에 값을 추가(append함수)

print(primes)
print("------------------------------------------------------------------------------------------")
#중첩 for문 소수
for i in range(2,101): #2부터 100까지
    is_prime = True #소수인 경우
    for j in range(2,i): # 2부터 시작하고 n+1이 아닌 이유는 소수의 특성상 약수의 개수가 2가 되는게 1과 n밖에 없으므로 1과 n을 제외(n-1)하여 시작.
        if i%j == 0: # 앞에서 제외를 했으므로 0으로 나누어 떨어지는게 만족을 해버리면 소수가 아니라는 뜻
            is_prime = False #소수가 이닌 경우
            break
    if is_prime == True: #is prime이 True라면 그 값은 소수이고
        print(i,end=' ') #줄바꿈으로 i값을 출력
print()
print("------------------------------------------------------------------------------------------")
###중첩 while문 소수
i=2 #2부터 시작
while i<101: #100까지
    is_prime = True #소수인 경우
    j=2 #2부터 시작
    while (j < i): #j가 i값 보다 작을때까지 반복
        if i%j == 0: #나누어 떨어지면 소수가 아닌 합성수
            is_prime = False #소수가 아닌 경우
            break
        j+=1 #j값을 1올리고 다시 반복
    if is_prime == True: #만약 소수이면
        print(i,end=' ') #i값을 줄바꿈으로 출력하라
    i+=1

print()
print("------------------------------------------------------------------------------------------")
###중첩 for문 소수

for num in range(2, 31) : #2부터 30까지
    is_prime=True #소수인 경우
    for j in range(2,num): # 2부터 시작하고 n+1이 아닌 이유는 소수의 특성상 약수의 개수가 2가 되는게 1과 n밖에 없으므로 1과 n을 제외(n-1)하여 시작.
        if num % j == 0 : # 앞에서 제외를 했으므로 0으로 나누어 떨어지는게 만족을 해버리면 소수가 아니라는 뜻
            is_prime = False #소수가 이닌 경우
            break
    if is_prime: #is prime이 True라면 그 값은 소수이고
        print(num, ":소수") #소수를 출력
    else:
        print(num, ":합성수")#나머지는 합성수를 출력
print("------------------------------------------------------------------------------------------")

###중첩 while문 소수
i=2 #2부터 시작
while i<31: #100까지
    is_prime = True #소수인 경우
    j=2 #2부터 시작
    while (j < i): #j가 i값 보다 작을때까지 반복
        if i%j == 0: #나누어 떨어지면 소수가 아닌 합성수
            is_prime = False #소수가 이닌 경우
            break
        j+=1 #j값을 1올리고 다시 반복
    if is_prime == True: #만약 소수이면
        print(i, "소수") #i값과 소수를 출력
    else: #나머지는
        print(i, "합성수")# i값과 합성수를 출력
    i+=1