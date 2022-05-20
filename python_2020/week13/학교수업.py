#1번
def sum(v1,v2):
    result = 0
    result =v1+v2
    return result
print(sum(1,2))

#2번 설명
def div(a,b):
    return a/b

print(div(10,2))

#뒤에 디폴트 값 주기
def div(a,b=1):
    return a/b

print(div(10))


#앞에 디폴트 값 주기
#def div(a =1 ,b): #파라메타의 디폴트 값을 줄때는 뒤에서부터 줘서 오류가 뜸
    #return a/b

#print(div(10))

#2번

def func(v1,v2=0,v3=0):
    return v1+v2+v3
print(func(1))
print(func(1,2))
#print(func(())

#3번
a=0
def func1():
    print(a)
def func2():
    a=111
    print(a)
func1()
func2()

#4번

#저번에 배운거
num = int(input("숫자를 입력:"))
fact = 1
for i in range(1, num+1):
    fact*=i
    print("%d!=%d"%(i, fact))

#문제
def factorial(n):
    fact = 1
    for i in range (1, n+1):
        fact*=i
    return fact

num = int(input("수를 입력:"))
print("%d!=%d"%(num, factorial(num)))

#5번
def sum(a):
    hap = 0
    for i in range(len(a)):
        hap += a[i] #리스트이기 때문에 i붙여야함
    return hap
num = [40,70,125,70,30,90]
print("합 =",sum(num))
print("평균:",sum(num)/len(num))

