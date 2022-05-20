#1418083 최희태 
a = int(input("\"숫자입력1(a)\"\n=>"))
b = int(input("\n\"숫자입력2(b)\"\n=>"))
print("\n1번(a) 숫자 {0}, 2번(b) 숫자 {1}을 입력하셨습니다." .format(a,b))
result = a + b
print("%s" % "\n\" 더하기는 " "%d" % result,"\""",", end=" ")
result = a - b
print("%s" % "\" 빼기는 " "%d" % result,"\""",", end=" ")
result = a * b
print("%s" % "\" 곱하기는 " "%d" % result,"\""",", end=" ")
result = a / b
print("%s" % "\" 나누기는 " "%d" % result,"\"", "입니다.") 
