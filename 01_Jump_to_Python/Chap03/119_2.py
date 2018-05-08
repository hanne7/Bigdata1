# coding: cp949

card = input("카드를 소유하고 있습니까? (y/n): ")
partnership = input("아키텍쳐 택시 전용입니까? (y/n): ")
if card == 'y':    card = True
else:              card = False
if partnership == 'y':    partnership = True
else:              partnership = False

#if card == True:
#    if partnership == True:
#        print("택시를 타고 가실 수 있습니다.")
# 12번 라인이 동일하게 처리되므로 중첩된if를 사용할 필요가 없음

#if card and partnership == True: <-x 개별로 조건을 지정해야함
if card == True and partnership == True:
    print("택시를 타고 가실 수 있습니다.")
else:
    print("걸어가셔야 합니다.") 
