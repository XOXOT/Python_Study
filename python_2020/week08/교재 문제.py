## 변수 선언 부분 ##
i, k, heartNum = 0, 0, 0  # i와 k변수, 하트의 개수를 세는 hearNum 변수
numStr, ch, heartStr = "", "", ""  # 입력받을 숫자를 위해 numStr 변수와 하트를 저장할 heartStr 변수를 준비, 1개씩 분리한 숫자를 저장한 변수인 ch 준비

## 메인 코드 부분 ##
if __name__ == "__main__": ## 메인 함수 선언
    numStr = input("숫자를 여러 개 입력하세요 : ")  # 숫자로 구성된 문자열을 입력
    print("")  # 한줄 띄우기
    i = 0  # 아우터 제어변수를 위해 사용할 숫자
    ch = numStr[i]  # 숫자 i에 해당하는 리스트를 ch에 저장한다 - 글자
    while True:  #무한 반복
        heartNum = int(ch)  # ch에 저장된 글자를 숫자로 변경

        heartStr = ""  # 하트를 저장할 문자열을 초기화
        for k in range(0, heartNum):  # 12행의 추출한 숫자만큼 반복
            heartStr += "\u2665"  # 하트를 heartStr에 계속 누적
            k += 1

        print(heartStr)  # 저장한 하트를 출력

        i += 1
        if i > (len(numStr)-1):  #len 함수를 사용하여 numStr의 문자열 길이를 반환하여 i에 -1 한 수보다 커지면
            break  # 무한 반복을 빠져나온다

        ch = numStr[i]  # 입력한 숫자 중에서 다음 차례의 숫자를 추출해서 처리한다

print("------------------------------------------------------------------------------------------")

## 변수 선언 부분 ##
i, k, starNum = 0, 0, 0  # i와 k변수 , 별의 개수를 세는 starNum 변수
numStr, ch, starStr = "", "", ""  # 입력받을 숫자를 위해 numStr 변수와 별을 저장할 starStr 변수를 준비, 1개씩 분리한 숫자를 저장한 변수인 ch 준비

## 메인 코드 부분 ##
if __name__ == "__main__": ##메인 함수 선언
    numStr = input("숫자를 여러 개 입력하세요 : ")  # 숫자로 구성된 문자열을 입력
    print("")  # 한줄 띄우기
    i = 0  # 바깥쪽 반복문을 위해 사용할 숫자
    ch = numStr[i]  # 숫자 i에 해당하는 리스트를 ch에 저장한다 - 글자
    while True:  # 반복 수행
        starNum = int(ch) # ch에 저장된 글자를 숫자로 변경

        starStr = ""  # 별을 저장할 문자열을 초기화
        for k in range(0, starNum * 2):  # 40행의 추출한 숫자의 2배 만큼 반복
            starStr += "\u2605"  # 별을 starStr에 계속 누적
            k += 1

        print(starStr)  # 저장한 별를 출력

        i += 1
        if (i > len(numStr) - 1):  #len 함수를 사용하여 numStr의 문자열 길이를 반환하여 i에 -1 한 수보다 커지면
            break  # 무한 반복을 빠져나온다

        ch = numStr[i]  # 입력한 숫자 중에서 다음 차례의 숫자를 추출해서 처리한다
