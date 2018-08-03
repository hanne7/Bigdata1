while True:
    age = input("나이를 입력하세요. : ")
    if age == '종료':
        print('종료합니다.')
        break
    elif int(age) < 3:
        print("무료입니다.")
    elif int(age) <= 12:
        print("입장권은 10달러입니다.")
    elif int(age) >= 13:
        print("입장권은 15달러입니다.")