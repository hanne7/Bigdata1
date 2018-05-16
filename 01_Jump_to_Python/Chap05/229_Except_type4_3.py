num1=1
num2=0
system_error_message=''
print("업무1")
# f = open('나있는파일','r')
try:
    f = open('나있는파일','r')
    result=num1/num2
    print("업무2")
    f.close()
except FileNotFoundError as e:
    print("""
[알림]
'나없는파일'은 존재하지 않습니다.
정상 수행을 위해 파일을 준비하세요.
""")
    system_error_message=e
except ZeroDivisionError as e:
    print("""
[알림]
숫자를 0으로 나누어서는 안됩니다. num2의 값을 확인해보세요.
""")
    system_error_message=e
finally:
    if system_error_message:
        print("[시스템 에러메세지]")
        print(system_error_message)
    print("명령어 블록 수행완료")

print("프로그램 정상 종료.")
