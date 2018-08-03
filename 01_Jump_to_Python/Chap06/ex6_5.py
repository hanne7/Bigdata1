def numAdd(num1, num2):
    return num1 + num2
def numSub(num1, num2):
    return num1 - num2
def numMul(num1, num2):
    return num1 * num2
def numDiv(num1, num2):
    try:
        result = num1 / num2
    except:
        print("죄송합니다. 두 번째 입력에서 0을 입력하셨습니다. 분모는 0이 되어서는 안됩니다.")
    return result

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
            print("덧셈 결과 : %d"%numAdd(num1, num2))
            print("뺄셈 결과 : %d"%numSub(num1, num2))
            print("곱셈 결과 : %d"%numMul(num1, num2))
            print("나눗셈 결과 : %f"%numDiv(num1, num2))

        except:
            if isNumber(nums[0])==False and isNumber(nums[1])==True:
                print("1번째 입력이 [%s]입니다. 숫자를 입력하세요"%nums[0])
            elif isNumber(nums[0])==True and isNumber(nums[1])==False:
                print("2번째 입력이 [%s]입니다. 숫자를 입력하세요" % nums[1])
            elif isNumber(nums[0])==False and isNumber(nums[1])==False:
                print("1번째 입력이 [%s]입니다. 숫자를 입력하세요\n2번째 입력이 [%s]입니다. 숫자를 입력하세요"%(nums[0],nums[1]))