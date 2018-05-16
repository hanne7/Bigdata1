class Restaurant:
    def __init__(self, name, type):
        f = open('고객서빙현황로그.txt', 'r', encoding = 'UTF-8')
        self.number_served = int(f.readline())
        f.close()
        self.order_list = []
        self.restaurant_name = name
        self.cuisine_type = type
        self.todays_customer = 0
        self.f = open('고객서빙현황로그.txt', 'w', encoding='UTF-8')

    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 %s 이고 %s 전문점입니다."%(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요." % self.restaurant_name)

    def reset_number_served(self, number):
        self.todays_customer = number

    def increment_number_served(self, number):
        self.todays_customer += number

    def check_customer_number(self):
        print("지금까지 총 %d명 손님께서 오셨습니다.\n"%self.todays_customer)

    def order_menu(self):
        menu = '음식'
        print("%s을 주문하셨습니다.\n"%menu)

    def __del__(self):
        print("\n%s 레스토랑 문닫습니다.\n\n이용해 주셔서 감사합니다."%self.restaurant_name)
        self.f.write("%d\n" %(self.number_served + self.todays_customer))
        self.f.close()


class Korean_Rest(Restaurant):
    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 %s 이고 한식 전문점입니다."%self.restaurant_name)

    def order_menu(self, order):
        if order == 0:
            print(self.order_list)
            print("주문완료하셨습니다.")
            return
        elif order == 1:
            self.menu = '김치찌개'
        elif order  == 2:
            self.menu = '된장찌개'
        elif order  == 3:
            self.menu = '순두부찌개'
        elif order  == 4:
            self.menu = '동태찌개'
        elif order  == 5:
            self.menu = '공기밥'
        print("%s 주문하셨습니다." % self.menu)
        self.order_list.append(self.menu)


class Japanese_Rest(Restaurant):
    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 %s 이고 일일식 전문점입니."%self.restaurant_name)

    def order_menu(self, order):
        if order == 0:
            print(restaurant.order_list)
            print("주문완료하셨습니다.")
            return
        elif order == 1:
            self.menu = '스시'
        elif order  == 2:
            self.menu = '돈가스'
        elif order  == 3:
            self.menu = '우동'
        elif order  == 4:
            self.menu = '라멘'
        elif order  == 5:
            self.menu = '규동'
        print("%s 주문하셨습니다." % self.menu)
        self.order_list.append(self.menu)

name, type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : ").split()
if type == 'k':
    restaurant = Korean_Rest(name, type)
elif type == 'j':
    restaurant = Japanese_Rest(name, type)
else:
    restaurant = Restaurant(name, type)

restaurant.describe_restaurant()
open = input("레스토랑을 오픈하시겠습니까? (y/n) : ")
if open == 'y':
    restaurant.open_restaurant()
    while True:
        option = str(input("어서오세요. 몇명이십니까?(초기화:0입력, 종료:-1, 누적고객 확인:p) : "))
        if option == '0':
            restaurant.reset_number_served(0)
            print("손님 카운팅을 0으로 초기화 하였습니다.\n")
        elif option == '-1':
            print("\n주문받겠습니다.\n")
            break
        elif option == 'p':
            restaurant.check_customer_number()
        else:
            print("손님 %d명 들어오셨습니다. 자리를 안내해드리겠습니다.\n" % int(option))
            restaurant.increment_number_served(int(option))

    while True:
        if isinstance(restaurant, Korean_Rest):
            order = int(input("메뉴를 선택하십시오.\n1.김치찌개\n2.된장찌개\n3.순두부찌개\n4.동태찌개\n5.공기밥\n메뉴번호 입력(0=주문종료) : "))
        elif isinstance(restaurant, Japanese_Rest):
            order = int(input("메뉴를 선택하십시오.\n1.스시\n2.돈가스\n3.우동\n4.라멘\n5.규동\n메뉴번호 입력(0=주문종료) : "))
        print()
        restaurant.order_menu(order)

        if order == 0:
            break

