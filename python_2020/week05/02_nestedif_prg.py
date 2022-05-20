###1418083 최희태

score = int(input("점수 입력 =>"))
grade =' '
if score >=90:
    grade = 'A'
elif score >=80:
    grade = 'B'
elif score >=70:
    grade = 'C'
elif score >=60:
    grade = 'D'
else:
    grade = 'F'

print("%d점수, %c 학점 입니다" % (score, grade))
