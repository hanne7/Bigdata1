while True:
    num = input("세 개의 양수를 입력하세요 (종료 -1): ")
    if num == '-1':
        print("종료합니다")
        break
    else:
        nums = num.split(' ')
        if int(nums[2])%int(num[0])==0 and int(nums[2])%int(nums[1])==0:
            print('%d는 %d와 %d의 공배수입니다.'%(int(nums[2]), int(nums[0]), int(nums[1])))
        else:
            print('%d는 %d와 %d의 공배수가 아닙니다.' % (int(nums[2]), int(nums[0]), int(nums[1])))

