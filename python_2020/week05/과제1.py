###1418083 최희태

score1 = int(input("과목1 점수 입력 =>"))
score2 = int(input("과목2 점수 입력 =>"))
avg = (score1+score2)/2
grade = ' '
if avg >=90:
    grade = 'A'
elif avg >=80:
    grade = 'B'
elif avg >=70:
    grade = 'C'
elif avg >=60:
    grade = 'D'
else:
    grade = 'F'

print("평균점수 %d , %c 학점 입니다" % (avg, grade))
