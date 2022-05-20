date=[]
data=list((input("데이터를 입력하세요")).split())
data = list(map(int,data))
print(data)

def sum(a):
    hap = 0
    for i in a:
        hap+= i
        return hap
num=[40,70,125,70,30,90]
print("합",sum(data))
print("평균", sum(data)/len(data))