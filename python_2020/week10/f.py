is_prime = True
num = 7
for i in range(2, num) :
    if num % i == 0 :
        is_prime = False
print(is_prime)