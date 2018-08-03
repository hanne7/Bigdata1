polls = []
while True:
    q = input("프로그래밍이 왜 좋으세요?(종료 입력시 프로그램 종료): ")
    if q != '종료':
        name = input("이름을 입력해주세요 : ")
        print("설문에 응답해 주셔서 감사합니다.")
        print("[%s] %s" % (name, q))
        a = '[' + name + ']' + ' ' + q
        polls.append(a)
    else:
        print("프로그램 종료")
        f = open('poll.txt', 'w', encoding='UTF-8')
        for poll in polls:
            f.write(poll + '\n')
        f.close()
        break
