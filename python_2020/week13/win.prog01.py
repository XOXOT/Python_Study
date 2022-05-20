#1418083 최희태
from tkinter import * #*는 전체를 의미

#함수선언
def ok():
    label2["text"] = "안녕 ~~~~ 파이썬"

w = Tk() #윈도우를 반환
w.title('1418083 최희태') #창 제목

#위젯 배치
photo = PhotoImage(file ="dog.gif") #, width = 300, height = 100 사이즈 조절 가능
label1 = Label(w, text="경영학과 최희태") #label1은 레이블을 만들어주는 변수이고 Label 함수는 레이블을 만들어주는 것
label2 = Label(w, text="재미있는 파이썬", font=("맑은고딕", 35), fg="red")
label3 = Label(w, image = photo)
button = Button(w, text="확인", command = ok) #확인 버튼 생성
btnQuit = Button(w, text="종료", command = quit) #종료 버튼
label1.pack() #pack함수는 해당 레이블을 화면에 표시
label2.pack()
label3.pack()
button.pack()
btnQuit.pack()
w.geometry("1000x500") #윈도의 크기 지정 폭x높이
w.resizable(width=False,height=False) #창조절 불가 기본값은 True로 되어있다.
w.mainloop() #이벤트 루핑 수행