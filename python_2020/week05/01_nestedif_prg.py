score = int(input("점수 입력 =>"))
grade =' '
if score >=90:
    grade = 'A'
else:
    if score >=80:
        grade = 'B'
    else:
        if score >=70:
            grade = 'C'
        else:
            if score >=60:
                grade = 'D'
            else:
                grade = 'F'

print("%d점수, %c 학점 입니다" % (score, grade))
