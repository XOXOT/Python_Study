####### 14주차 조별 과제 8조 2016746 조수예 2017274 조대식 2016691 박선하 1418083 최희태 #
#발표자 2017274 조대식 #
#제목 베스킨라빈스31 #
from tkinter import * #tkinter import 함
from tkinter import messagebox #messagebox 모듈을 가져옴.

w = Tk() #창(컨테이너)를 생성
w.title("베스킨라빈스31 주문 프로그램")  # 창 제목 설정
w.geometry("550x750")   #윈도우 크기 결정, 폭 x 높이

## 함수 선언
def fun1() : # fun1함수는 chk.get() 함수로 체크버튼에 설정된 값을 가져와서 메시지를 출력한다.
    if chk1.get() == 1 :
        menu1 ="이달의메뉴"
    else :
        menu1=""
    if chk2.get() == 1 :
        menu2 = "사랑에빠진딸기"
    else :
        menu2 = ""
    if chk3.get() == 1 :
        menu3 = "초콜릿무스"
    else :
        menu3 = ""
    if chk4.get() == 1 :
        menu4 = "뉴욕치즈케이크"
    else :
        menu4 = ""
    if chk5.get() == 1 :
        menu5 = "엄마는외계인"
    else :
        menu5 = ""
    if chk6.get() == 1 :
        menu6 = "수퍼팽귄시리얼"
    else :
        menu6 = ""
    messagebox.showinfo('아이스크림 메뉴', menu1 + " " + menu2 + " " + menu3 + " " + menu4 + " " + menu5 + " " + menu6) #메시지 박스의 정보를 보여주는 것
    lal1["text"]="아이스크림 메뉴 : " + menu1 + " " + menu2 + " " + menu3 + " " + menu4 + menu5 + " " + menu6
def fun2() : # fun2 함수는 var 변수 값으로 맨 아래쪽 레이블의 텍스트를 변경한다.
    if rVar.get() ==1 :
        lang = "파인트 7200원"
    elif rVar.get() == 2:
        lang = "쿼터 15500원"
    elif rVar.get() == 3:
        lang = "패밀리 21000원"
    else :
        lang = "하프갤런 26500원"
    messagebox.showinfo('아이스크림 사이즈와 가격', lang)
    lal2["text"] = "아이스크림 사이즈와 가격 : " + lang

## main 코드 작성
lal1 = Label(w, text="아이스크림 메뉴", fg="purple")
photo = PhotoImage(file = "ice.gif", width=500, height=300)  #사진 삽입 width=가로, height=세로
label1 = Label(w, image = photo) #Label()의 옵션 image에서 속성을 지정하면 해당 이미지를 글자 대신에 사용한다.
#Checkbutton 위젯사용하기
chk1 = IntVar() #chk 변수를 준비하는 데 IntVar()함수를 사용
ch1 = Checkbutton(w, text="이달의메뉴", variable=chk1)  # Checkbutton()의 옵션 중에서 variable에 chk변수를 사용한다.
chk2 = IntVar()
ch2 = Checkbutton(w, text="사랑에빠진딸기", variable=chk2)
chk3 = IntVar()
ch3 = Checkbutton(w, text="초콜릿무스", variable=chk3)
chk4 = IntVar()
ch4 = Checkbutton(w, text="뉴욕치즈케이크", variable=chk4)
chk5 = IntVar()
ch5 = Checkbutton(w, text="엄마는외계인", variable=chk5)
chk6 = IntVar()
ch6 = Checkbutton(w, text="수퍼팽귄시리얼", variable=chk6)

##Radiobutton 위젯사용하기
lal2 = Label(w, text="아이스크림 사이즈와 가격", fg="red")
rVar = IntVar() #Radiobutton 변수 준비, 정수형 변수 rVar를 준비한다.
rbutton1 = Radiobutton(w, text="파인트", variable=rVar, value=1) # 각 라디오 버튼을 선택하면 var에는 value에 할당된 값이 들어간다.
rbutton2 = Radiobutton(w, text="쿼터", variable=rVar, value=2) # rbutton1 버튼을 선택하면 var에는 1이 대입된다.
rbutton3 = Radiobutton(w, text="패밀리", variable=rVar, value=3)
rbutton4 = Radiobutton(w, text="하프갤런", variable=rVar, value=4)

btnOk = Button(w, text="아이스크림 선택 후 누르세요",  fg="#ff00ff" , command=fun1)
btnOk1 = Button(w, text="아이스크림 사이즈와 가격", fg="#ff0000" , command=fun2)  #=16진수,#ff=4비트, #ffffff=흰색, #ff0000=빨강, #00ff00=그린, #ffff00=노랑

label1.pack()
lal1.pack()
ch1.pack()
ch2.pack()
ch3.pack()
ch4.pack()
ch5.pack()
ch6.pack()
lal2.pack()
rbutton1.pack()
rbutton2.pack()
rbutton3.pack()
rbutton4.pack()
btnOk.pack()
btnOk1.pack()

w.mainloop() #이벤트 루프 생성하기(대기)