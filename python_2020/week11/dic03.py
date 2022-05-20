foods = {"떡볶이": "오뎅",
         "짜장면" : "단무지",
         "라면" : "김치",
         "피자" : "피클",
         "맥주" : "땅콩",
         "치킨" : "치킨무",
         "삼겹살" : "상추"}
while(True): #무한반복
    myfood = input(str(list(foods.keys())) + "중 좋아하는 음식은? ")
    if myfood in foods:
        print("%s 궁합음식은 %s 입니다" % (myfood, foods.get(myfood)))  ##키값 출력은 foods['키값'] or foods.get(키값)
    elif myfood == "끝": #끝을 입력해야지 무한반복끝
        break
    else :
        print("그런 음식이 없습니다. 확인해보세요")