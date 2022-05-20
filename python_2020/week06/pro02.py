###1~20까지 합을 계산하는 프로그램

hap = 0
for i in range(1,21): #range(1,21,2)는 홀수의 합 range(2,21,2)는 홀수의 합 
    hap +=i

print("1~20까지 합 = %d"%hap)

print("===================")

number = [11,22,33,44,55,66]

for n in number:
    print(n, end ='   ')
