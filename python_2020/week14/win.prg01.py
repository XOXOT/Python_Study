from tkinter import * #tkinter import함
from tkinter import messagebox #messagebox 모듈을 가져옴


def fun_ok():
    lblInfo["text"] = "안녕하세요~~ Ok 버튼을 클릭했습니다."
def fun_cancel():
    lblInfo["text"] = "Cancel 버튼을 클릭했습니다." #funtion 입력

#메시지 박스
def fun_mess():
    messagebox.showinfo("정보확인", "안녕하세요 최희태입니다.")
def fun_question():
    result = messagebox.askyesno("선호도", "파이썬을 좋아하나요?") #askquestion은 yes와 no로 표현됨
    print(result) #확인을 해보면 True와 False가 나옴
    if result== True: # yes가 아니라 true로 바꿔야함
        lblInfo.configure(text="파이썬을 사랑합니다")
    else:
        lblInfo["text"]="ㅜㅜㅜ 슬퍼요"

window =Tk() # 창을 생성
window.geometry("300x150")
lblInfo = Label(window,text="알람입니다")
btnOk = Button(window, text = "Ok", fg = "blue",command=fun_ok) #Button 위젯(컴포넌트)를 생성
btnCancel = Button(window, text="Cancel", fg = "#ff0000",command=fun_cancel) #빨강
#color(디지털) = 기본 rg  red, grenn, blue (1byte) #의 의미는 16진수로 표현한다는 것 #ff는 f하나 당 4bit 즉 #ff는 8비트
# #ff0000 - 여기서 ff는 빨강색이고 나머지는 0이니까 빨강
# #00ff00 - 중간 ff니까 그린 , #ffff00는 노랑
btnMessage = Button(window, text="message", command=fun_mess)
btnAsk = Button(window, text="파이썬선호도", command=fun_question)

#배치, 정렬, 조정
#side=TOP은 수직정렬 중 위에서 아래 side=BOTTOM은 밑에서 위로 정렬 side=LEFT,side=RIGHT는 버튼을 왼쪽 오른쪽 배치
#fill=X는 대문자 X로 해야하고 윈도우 폭에 맞게 버튼을 맞춤
#padx와 pady는 위젯 사이의 여백을 조절해줌 ex)padx=10, pady=10 (숫자는 픽셀값)
#ipadx와 ipady는 위젯 내부에 여백을 주는 것
#절대적인 위치를 주고 싶을 때는 pack대신 place를 넣어야함

lblInfo.pack()
btnOk.place(x=100,y=0)
btnCancel.pack(side=BOTTOM)
btnMessage.pack(side=BOTTOM,padx=5,pady=5)
btnAsk.pack(side=RIGHT,padx=5,pady=5) 

window.mainloop() #이벤트 루프 생성(대기)