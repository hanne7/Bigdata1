def compare(num):
    if num%10 == 0:
        return True
    else:
        return False

while True:
    num = int(input("양수를 입력하세요(종료 -1) : "))
    if num == -1:
        print("종료합니다.")
        break
    else:
        print(compare(num))