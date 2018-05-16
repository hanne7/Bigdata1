class Restaurant:
    def __init__(self, name, type):
        self.number_served = 0
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 %s 이고 %s 전문점입니다."%(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요." % self.restaurant_name)

    def reset_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

    def check_customer_number(self):
        print("지금까지 총 %d명 손님께서 오셨습니다.\n"%self.number_served)

    def __del__(self):
        print("%s 레스토랑 문닫습니다."%self.restaurant_name)

name, type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : ").split()

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
            break
        elif option == 'p':
            restaurant.check_customer_number()
        else:
            print("손님 %d명 들어오셨습니다. 자리를 안내해드리겠습니다.\n" % int(option))
            restaurant.increment_number_served(int(option))