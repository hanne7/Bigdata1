# coding: cp949

coffee_number = 10
menu = """
        <Menu>
        1. 커피구매
        2. 커피잔량확인
        3. 프로그램 종료
        메뉴를 선택하세요 : """

while True:

    print(menu,end='')
    menu_number = int(input())

    if menu_number == 1:
        money = int(input("\n금액을 입력하세요: "))
        if money == 300:
            print("커피를 줍니다.")
            coffee_number = coffee_number - 1
        elif money > 300:
            print("커피를 줍니다.\n여기 거스름돈 %d원 입니다." % (money - 300))
            coffee_number = coffee_number - 1
        else :
            print("금액이 모자랍니다.")

    elif menu_number == 2:
        print("남은 커피의 양은 %d개 입니다." % coffee_number)           
    elif menu_number == 3:
        print("프로그램을 종료합니다.\n")
        break    
    
    if not coffee_number:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
