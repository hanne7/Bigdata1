def input_ingredient():
    ingredient_list = []
    while True :
        ingredient = input("안녕하세요. 원하시는 재료를 입력하세요: ")
        if ingredient == "종료":
            return ingredient_list
        ingredient_list.append(ingredient)


def make_sandwiches(ingredient_list):
    print("\n샌드위치를 만들겠습니다.")
    for i in ingredient_list:
        print(i + " 추가합니다.")
    print("여기 주문하신 샌드위치를 만들었습니다. 맛있게 드세요.\n")


while True :
    menu = int(input("안녕하세요 저희 가게에 방문해 주셔서 감사합니다.\n1. 주문\n2. 종료\n입력: "))

    if menu == 1:
        a = input_ingredient()
        make_sandwiches(a)

    if menu == 2:
        print("프로그램 종료합니다.")
        break





