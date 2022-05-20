menu={} # 딕셔너리 변수로 선언
menu['Americano'] = ': 가격 3000원'    #딕셔너리에 키값과 밸류값 선언
menu['Ice Americano'] = ': 가격 3500원'
menu['Cappuccino'] = ': 가격 4000원'
menu['Caffe Latte'] = ':가격 4500원'
menu['Espresso'] = ': 가격 3600원'

for i in menu.keys() :
    print("%s %s" % (i, menu[i]))

while(True) : #무한반복을 위해 와일에 트루를 지정함
    kmenu = input("위의 메뉴를 선택하시오")
    if kmenu in menu :
        print("<%s>는 <%s>입니다 결재 부탁드립니다 "%(kmenu,menu.get(kmenu)[5:9]))
    elif kmenu.upper() == 'END' :
        break
    else :
        print("미안합니다. %s은 메뉴는 없습니다" %(kmenu))