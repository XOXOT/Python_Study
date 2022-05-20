price = {'김밥':5000,'어묵':3000,'떡볶이':2000}
price['김밥']=7000
print(price)
print(price.keys())
print(len(price))
for k in price.keys():
    print("%s->%s"%(k,price[k]))
price['순대'] = 4500
print(price)

mydata={1,1,1,2,2,3,3,4,4,5}
mydata.add(5)
mydata.add(6)
print(len(mydata))

list1 = [n*10 for n in range(1,5)]
print(list1)
set1 = {n for n in range(1,11) if n%2==0}
print(set1)

print(type(list1))
print(type(price))

dic={}
dic['경영'] = 'management'
dic['정보'] = 'information'
dic['자료'] = 'data'
dic['틀'] = 'frame'
dic['초점'] = 'focus'
dic['기초'] = 'basic'
dic['자동차'] = 'car'
while(True):
    mydic = input(str(list(dic.keys())) + "중 찾고 싶은 단어는?")
    if mydic in dic:
        print("<%s>의 영어단어는 <%s> 입니다"%(mydic,dic.get(mydic)))
    elif mydic.upper() =='END': #
        break
    else:
        print("해당하는 단어를 찾을 수 없습니다.")
