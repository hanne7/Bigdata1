# coding: cp949

#money = 1
#money = 7
money = 0 
if money:
    print("택시를 타고 가라")
#    print("도착했습니다") <- indentation 이 맞지 않아 에러
#    print("도착했습니다.")
else:
    print("걸어 가라")
#  print("도착했습니다") <- indentation 에러
#    print("도착했습니다.") <- 동일 코드 중복.
                            # 프로그램 수정시 동일 코드 로직 변경이 누락될 가능성 있음
print("목적지에 도착했습니다.") # <- 중복코드 제거
print("프로그램을 종료합니다.")
