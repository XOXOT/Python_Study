###1418083 최희태

fact = int(input("수를 입력하세요:"))
f=1
for i in range(1,fact+1):
    f*=i
    print(i,"! = %d" % f)


ss='python'
for i in range(0,len(ss)):
    print(ss[i]+'$',end='')

mystr = 'hanbit media, hanbit academy, hanbit life'

print(mystr.count('hanbit'))