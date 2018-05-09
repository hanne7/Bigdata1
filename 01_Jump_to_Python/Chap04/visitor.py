def search_visitor(name):
    f = open("방명록.txt", 'r', encoding='UTF-8')
    lines = f.readlines()
    for i in lines:
        if name in i:
            print(name + "님 다시 방문해 주셔서 감사합니다. 즐거운 시간되세요.")
            return

    birthday = input("생년월일을 입력하세요 : ")
    f = open("방명록.txt", 'a', encoding='UTF-8')
    data = name + " " + birthday + "\n"
    f.write(data)
    print(name + "님 환영합니다. 아래 내용을 입력하셨습니다.\n" + data)

while True:
    name = input("이름을 입력하세요: ")
    if name == '종료':
        print("종료합니다.")
        break
    search_visitor(name)


