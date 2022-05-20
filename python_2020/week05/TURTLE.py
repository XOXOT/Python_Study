import turtle as t #turtle의 모듈을 import하고 turtle을 t로 표기한다. 
import random as r # 난수  발생 모듈 import 

swidth, sheight = 500, 500 #스크린 크기 폭과 높이 
t.title("무지개 원그리기") # 제목 설정
t.shape("turtle") #모양 설정 
t.setup(width=swidth+50, height=sheight+50) #윈도크기 
t.screensize(swidth, sheight)
t.penup()
t.goto(0, -sheight/2)
t.pendown()
t.speed(6) # 제일 빠르게 
t.pencolor("red")
t.pensize(1) #굵기 
t.bgcolor("black") #배경색 

for i in range(1,100): 
    rand = r.randrange(1, 251) 
    if rand %3 ==1:
        t.pencolor("red")
        t.pensize(2)
    elif rand %3 ==2:
        t.pencolor("yellow")
        t.pensize(3)
    else:
        t.pencolor("orange")
        t.pensize(4)
    t.circle(rand)
    
    #t.circle(r)
    #t.circle(r.randrange(1,251)) #랜덤으로 증가, 감소함
    
#t.circle(50) #반지름
#t.circle(100)
#t.circle(150)
#t.circle(200)
#t.circle(250)
