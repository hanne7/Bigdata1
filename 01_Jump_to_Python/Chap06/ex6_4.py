def numAdd(num1, num2):
    return num1 + num2

def isNumber(num):
    try:
        int(num)/2
        return True
    except:
        return False

while True:
    num = input("두 수를 입력하세요. (종료: 프로그램종료): " )
    if num == '종료':
        print("프로그램 종료합니다.")
        break
    elif ' ' not in num:
        print("잘못입력하셨습니다. 두 수를 공백으로 구분하여 입력해주세요")
    else:
        try:
            nums = num.split(' ')
            num1 = int(nums[0])
            num2 = int(nums[1])
            print(numAdd(num1, num2))
        except:
            if isNumber(nums[0])==False and isNumber(nums[1])==True:
                print("1번째 입력이 [%s]입니다. 숫자를 입력하세요"%nums[0])
            elif isNumber(nums[0])==True and isNumber(nums[1])==False:
                print("2번째 입력이 [%s]입니다. 숫자를 입력하세요"%nums[1])
            else:
                print("1번째 입력이 [%s]입니다. 숫자를 입력하세요\n2번째 입력이 [%s]입니다. 숫자를 입력하세요"%(nums[0],nums[1]))