n = int(input("숫자를 입력하라"))

is_prime = 0
for num in range(1, n+1) :
    if n % num ==0 :
        is_prime=is_prime+1
if is_prime == 2:
    print("소수입니다.")
else:
    print("소수가 아닙니다.")

print("------------------------------------------------------------------------------------------")

###1418083 최희태

n = int(input("숫자를 입력하라"))

is_prime = True #소수인 경우
for num in range(2, n) : #2부터 시작하고 n+1이 아닌 이유는 소수의 특성상 약수의 개수가 2가 되는게 1과 n밖에 없으므로 1과 n을 제외(n-1)하여 시작.
    if n % num ==0 : #앞에서 제외를 했으므로 0으로 나누어 떨어지는게 만족을 해버리면 소수가 아니라는 뜻
        is_prime = False # 소수가 아닌 경우
if is_prime==True :
    print(n, "는 소수입니다.")
else:
    print(n, "는 소수가 아닙니다.")

print("------------------------------------------------------------------------------------------")

###1418083 최희태

primes = [] #리스트 생성

for num in range(2, 101) : #2부터 100까지

    is_prime=True # 소수인 경우
    for j in range(2,num): #위의 1번과 같이 1과 n를 제외함
        if num % j == 0 : #위의 1번과 같이 0과 n를 제외를 했으므로 0으로 나누어 떨어지는게 만족을 해버리면 소수가 아니라는 뜻
            is_prime = False #소수가 이닌 경우

    if is_prime: #is prime이 True라면 그 값은 소수이고
        primes.append(num) #primes리스트에 값을 추가(append함수)

print(primes)