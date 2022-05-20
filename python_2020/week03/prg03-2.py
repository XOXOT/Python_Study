#### 변수 선언 #근데 변수 선언 안해도 나오긴 나옴...
money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

## main code
money = int(input("교환할 돈은 얼마 ?"))

c500 = money // 500
money %= 500 # 이것도 안적어도 나오긴 나옴 

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money //10
money %= 10

print("500원 : %d 개 " % c500) 
print("100원 : %d 개 " % c100)
print("50원 : %d 개 " % c50)
print("10원 : %d 개 " % c10)
print("잔돈 : %d원 " %money)
