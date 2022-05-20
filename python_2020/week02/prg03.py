#1418083 최희태 
a = 10
b = 50.85
c = True
d = "동아대학교"
f = [ ] #list type을 선언
e = () #tuple type을 선언 
A = 40 #변수명은 대소문자 구분
#1b = 90.87 ==> 식별자는 첫문자가 숫자일 수 없음 
print(a,b)
print(type(a), type(b), type(c), type(d))
print(type(f), type(e))

a = a + 200
print(a) 

#turtle graphics programing
import turtle as t #모듈을 가져옴 as를 쓰면 turtle을 t로 약어로 쓸 수 있음 

t.shape('turtle')
t.color('red') #줄 색은 빨강색 
t.forward(200)#앞으로 200픽셀 이동 
t.right(90) #오른쪽으로 90도 회전 
t.forward(200)
t.right(90)
t.forward(200)
turtle.right(90) # t로 정의를 내려서 turtle을 쓰면 에러가 남 
turtle.forward(200)
