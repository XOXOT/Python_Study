student1 = {'학번' : 1000, '이름': '홍길동', '학과': '경영정보학과'}

for k in student1.keys(): ##[학번, 이름, 학과]
    print("key %s -> value %s" % (k, student1[k])) #student1[k]는 그 키값의 value를 출력