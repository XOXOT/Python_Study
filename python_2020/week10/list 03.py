a1=[]
a2=[]
value=0
for r in range (4):  #행
    for c in range (5): #열
        a1.append(value)
        value += 3
    a2.append(a1)
    a1=[]
print(a2)
for r in range(4):
    for c in range(5):
        print(a2[r][c], end="     ")
    print()
