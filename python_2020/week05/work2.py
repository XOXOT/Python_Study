import random as r #난수 발생 모듈

a, b = 0,0 # 변수 지정 

a = r.randrange(1, 7)  #1~6까지 난수 발생시켜 변수에 대입 
b = r.randrange(1, 7)

print("a=%d, b=%d"%(a, b))

if a>b:
    print("a가 b를 이겼습니다.")
elif a<b:
    print("b가 a를 이겼습니다.")
else:
    print("a와 b가 비겼습니다.")
