# coding: cp949

money = int(input("얼마를 갖고 있습니까? "))
card = input("카드를 소유하고 있습니까? (y/n): ")
if card == 'y':    card = True
else:              card = False

if money >= 3000:
    print("택시를 타고 가라")
else:
    if card == True:
#        print("택시를 타고 가라") # 동일 코드 중복
        print("카드 지원 택시. 택시 타고 가라") # 중복코드 아닌 경우 허용
    print("걸어 가라")
