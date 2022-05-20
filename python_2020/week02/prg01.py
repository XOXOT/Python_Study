#1418083 최희태
#input() print() 함수 이해하기 
#a=input("숫자입력1=>") #input은 문자열이므로 더하면 a가 80 b가 100이면 80100이 나옴 
#b=input("숫자입력2=>") #input의 +는 연결, 결합에 대한 문자이다. 그래서 int()를 활용해야한다.  
#result = a + b
#print("덧셈", result)
#result = a * b
#print("곱셈", result)
#정수형: int()
#실수형 float()
#문자형: str()
#논리형: boolean()
#오류 수정
a=int(input("숫자입력1=>"))
b=int(input("숫자입력2=>"))
result = a + b
print("덧셈", result)     #+,-,*(곱하기), /(나누기)
result = a - b
print("뺄셈", result)
result = a * b
print("곱셈", result)
result = a / b
print("나눗셈", result)
