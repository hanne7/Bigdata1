# coding: cp949

money = int(input("얼마를 갖고 있습니까? "))
card = input("카드를 소유하고 있습니까? (y/n): ")
if card == 'y':    card = True
else:              card = False

if money >= 3000:
    print("아키텍쳐 택시 분석 조건을 분석합니다.")
    print("분석이 완료가 되었습니다.")
    print("택시를 타고 가라")
elif card == True:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
