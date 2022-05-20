#프로그래밍 02분반 8조 2016746 조수예 2017274 조대식 2016691 박선하 1418083 최희태
#발표자 2016746 조수예

menu={} #딕서녀리 변수로 선언
menu['Americano'] = ': 가격 3000원' #딕셔너리에 키값과 밸류값 지정
menu['Ice Americano'] = ': 가격 3500원'
menu['Cappuccino'] = ': 가격 4000원'
menu['Caffe Latte'] = ': 가격 4500원'
menu['Espresso'] = ': 가격 3600원'

for i in menu.keys() : #키값이랑 밸류값을 반복해서 출력하기 위해 for문을 입력
    print("%s %s" % (i, menu[i])) #i를 반복해서 출력함

while(True) : #무한반복을 위해 와일에 True값으로 지정함
    mymenu = input("위의 메뉴를 선택하시오.")
    if mymenu in menu : #딕셔너리에 있는 키값이 반복됨
        print("<%s>는 <%s>입니다 결재 부탁드립니다." %(mymenu,menu.get(mymenu)[5:9])) #menu.get(mymenu)와 같은 키 menu[mymenu]
                                                                                 #문자열을 인덱싱해서 5와 9로 값 설정했지만 가격이 10000원이 넘어가면 출력이 안됨.
    elif mymenu.upper() == 'END' : #계속 반복 될 때 멈추고 싶으면 end를 입력한다.
        break #END를 입력하면 브레이크가 걸림.
    else : #해당하는 단어가 아닌 딕셔너리에 없는 단어 입력 시 밑의 값 출력
        print("미안합니다. %s은 메뉴에 없습니다." %(mymenu)) #딕셔너리에 없는 단어 입력 시 mymenu의 값 적용

print(menu.keys())

