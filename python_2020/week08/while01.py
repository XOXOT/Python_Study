for i in range(1,4,1):
    print(i)

print("------------------------------------------------------------------------------------------")

i=1
while(i<4) :
    print(i)
    i+=1

print("------------------------------------------------------------------------------------------")

hap = 0
for i in range(1,11):
    hap += i
print("1~%d까지의 합 =%d"%(i,hap))

print("------------------------------------------------------------------------------------------")

i = 1
hap = 0
while i<=10: #10이 될 때까지 반복이라 11이면 빠져나옴
    hap += i
    i+=1
print("1~%d까지의 합 =%d"%(i-1,hap))