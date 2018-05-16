def get_customer_input():
    num1=1
    num2=-2
    if num1<0 or num2<0:
        raise NotImplementedError
    return num1+num2

result=0
try:
    get_customer_input()
except NotImplementedError:
    print("""[알림]
입력값에 음수가 들어왔습니다.
정상적인 연산을 위해서 입력값이 양수인지 확인하세요.""")

print("최종결과: %d"%result)