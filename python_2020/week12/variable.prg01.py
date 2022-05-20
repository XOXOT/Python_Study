### 전역변수와 지역변수###
def func1():
    a = 10 #함수 내에 변수를 선언하면 지역변수
    print("func1() a값", a, b)

def func2():
    global b ## 함수 안에 있는데 전역 변수로 사용하고 싶을때 글로벌 함수를 쓰면 된다.
    b = "동아대학교"
    print("func2() a값", a, b) ## a값이 없다고 오류남 #전역변수를 지정하면 전역변수가 들아감

###전역 변수
a =777
##메인코드

func2() #오류 변수가 없음
func1() #글로벌 변수가 func2에 있기 때문에 순서를 바꿔야함 만약 func위에 있다면 오류가 난다.