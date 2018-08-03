def read_content():
    f = open('poll.txt', 'r', encoding='UTF-8')
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()
def create_content(polls):
    f = open('poll.txt', 'w', encoding='UTF-8')
    for poll in polls:
        f.write(poll + '\n')
    f.close()

try:
    read_content()
except:
    while True:
        menu = input("기존 poll.txt 파일을 찾을 수 없습니다. 아래 중 선택하세요.\n1. 종료 2. 새로운 파일 생성 3. 변경된 파일경로 입력: ")
        if menu == '1':
            print('프로그램 종료')
            break
        elif menu == '2':
            polls = []
            while True:
                q = input("프로그래밍이 왜 좋으세요?(종료 입력시 프로그램 종료): ")
                if q != '종료':
                    name = input("이름을 입력해주세요 : ")
                    print("설문에 응답해 주셔서 감사합니다.")
                    a = '[' + name + ']' + ' ' + q
                    polls.append(a)
                    print("<현재 누적 응답 현황>")
                    for i in polls:
                        print(i)
                else:
                    print("프로그램 종료")
                    create_content(polls)
                    break
            break
        elif menu == '3':
            polls = []
            di = input("변경된 파일 경로를 입력하세요. : ")
            f = open(di + '/poll.txt', 'r', encoding='UTF-8')
            lines = f.readlines()
            print("<현재 누적 응답 현황>")
            for line in lines:
                print(line,end='')
            print()
            while True:
                q = input("프로그래밍이 왜 좋으세요?(종료 입력시 프로그램 종료): ")
                if q != '종료':
                    name = input("이름을 입력해주세요 : ")
                    print("설문에 응답해 주셔서 감사합니다.")
                    a = '[' + name + ']' + ' ' + q
                    polls.append(a)
                    print("<현재 누적 응답 현황>")
                    for line in lines:
                        print(line,end='')
                    for i in polls:
                        print(i)
                else:
                    print("프로그램 종료")
                    w = open(di + '/poll.txt', 'a', encoding='UTF-8')
                    for i in polls:
                        w.write(i + '\n')
                    w.close()
                    break
            f.close()
            break




