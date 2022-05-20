# https://github.com/sense64/python_basic01
# github에 실습파일이 있습니다.

a= 1000
b =78.95
#서식문자가 없는 경우
print(a, "   ", b)

#서식문자가 있는 경우 
print("%d" % a)
print("%5d" % a)
print("%05d" % a, end="  ") #end는 뒷자리 열 결과를  옆으로 출력한다. 즉 14번 열이 12번 열과 나란히 출력 

print("%f" % b) #일반 실수는 소수점 기본 6자리 
print("%07.1f" % b) #총 7자리 중 소수점이하의 자리는 한자리 
print("%07.3f" % b) #총 7자리 중 소수점이하의 자리는 3자리

print("%s" % "동아대학교")
print("%10s" % "경영정보학과")

#format() 함수 사용
print(format(a, "x")) #x는 16진수 
print("{1}, {0}" .format(a, b)) #a의 인덱스는 0이고 b의 인덱스가 1이므로 b부터 출력 
print("{1:5.1f} {0:5d}" .format(a, b)) #인덱스 1을 출력하는데 자릿 수는 5이고 소수 점 한자리까지 표현 즉 반올림. = 79.0, 인덱스 0을 출력하고 5자리 수 
