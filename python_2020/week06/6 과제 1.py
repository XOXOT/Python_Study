###1418083 최희태

evenhap = 0 
oddhap = 0

for i in range(1,101,1):
    if i%2==0:
        evenhap+=i
    else:
        oddhap+=i

print("1에서 100까지 짝수의 합:%d \n1에서 100까지 홀수의 합:%d" %(evenhap, oddhap))


print("======================")

###1418083 최희태

nums=[50,90,20,40,70,20]
hap = 0

for n in nums:
    hap += n
print("리스트[nums] 원소 값의 합:", hap) 
