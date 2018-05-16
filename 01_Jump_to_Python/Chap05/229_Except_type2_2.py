num1=1
num2=0
print("업무1")
# f = open('나있는파일','r')
try:
    result=num1/num2
    f = open('나있는파일','r')
    print("업무2")
except FileNotFoundError:
    print("""
[알림]
'나없는파일'은 존재하지 않습니다.
정상 수행을 위해 파일을 준비하세요.
""")
except ZeroDivisionError:
    print("""
[알림]
숫자를 0으로 나누어서는 안됩니다. num2의 값을 확인해보세요.
""")
print("프로그램 정상 종료.")
