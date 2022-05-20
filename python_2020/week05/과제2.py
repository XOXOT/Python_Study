###1418083 최희태

dust = int(input("미세먼지 농도를 입력하세요 ==>")) 
if dust >= 76:
    print("미세먼지 농도 %d ug / m^3로 매우 나쁨 입니다." %dust)
elif dust >= 36:
    print("미세먼지 농도 %d ug / m^3로 나쁨 입니다." % dust)
elif dust >= 16:
    print("미세먼지 농도 %d ug / m^3로 보통 입니다." % dust)
else:
    print("미세먼지 농도 %d ug / m^3로 좋음 입니다." % dust)
    
           
