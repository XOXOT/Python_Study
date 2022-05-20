from tkinter import *
from tkinter import messagebox

## 함수 선언
def fun1() :
    if chk1.get() == 1 :
        hobby1="독서"
    else :
        hobby1 =""
    if chk2.get() == 1 :
        hobby2 ="영화"
    else :
        hobby2 = "" #아니면 아무것도 아님
    messagebox.showinfo('최희태의 취미', hobby1 + "," + hobby2)
    lbl1["text"]="취미 : " + hobby1 + " " + hobby2

def fun2() :
    if rVar == 1 :
        lang = "파이썬"
    elif rVar == 2:
        lang = "C++"
    else :
        lang = "자바"
    messagebox.showinfo('내가 좋아하는 언어', lang)

w = Tk() #창(컨테이너)를 생성
w.title("1418083 최희태")
w.geometry("300x200")

## main 코드 작성
lbl1 = Label(w, text="결과", fg="red")

#Checkbutton 위젯사용하기
chk1 = IntVar() #변수준비
ch1 = Checkbutton(w,text="독서", variable=chk1)
chk2 = IntVar()
ch2 = Checkbutton(w,text="영화", variable=chk2)

##Radiobutton 위젯사용하기
rVar = IntVar() #Radiobutton 변수 준비
rbutton1 = Radiobutton(w, text="파이썬", variable=rVar, value=1)
rbutton2 = Radiobutton(w, text="C++", variable=rVar, value=2)
rbutton3 = Radiobutton(w, text="자바", variable=rVar, value=3)


btnOk = Button(w, text="누르세요", command=fun1)
btnOk1 = Button(w, text="좋아하는 언어", command=fun2)


lbl1.pack()
ch1.pack()
ch2.pack()
rbutton1.pack()
rbutton2.pack()
rbutton3.pack()
btnOk.pack()
btnOk1.pack()
w.mainloop()
