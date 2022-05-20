from tkinter import *
from tkinter import messagebox
#함수 선언
def grade () :
    score = int(num1.get()) #Entry 객체의 값을 가져와 정수형으로 변환함.
    if score >= 60 :
        result = "합격"
    else :
        result = "불합격"
    messagebox.showinfo("시험결과",result)

w = Tk()
w.geometry("200x50")
label = Label(w, text="점수 입력")
label.grid(column=0, row=0)
num1 = Entry(w, width=20) #Entry 클래스는 데이터를 입력 받을 수 있는 클래스
num1.grid(column=1,row=0) #grid(column=1,row=0)는 pack()을 대신하는 배치에 관련된 함수이다. grid함수는 column=1, row=1인경우 2번째 컬럼과 2번째 행에 배치함
button = Button(w, text="계산", command=grade)
button.grid(column=0, row=1)
w.mainloop()