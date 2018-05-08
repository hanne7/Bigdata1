var1 = 1

def vartest():
    global var1
    var1 = var1 + 1

def vartest2():
    print(var1)

def vartest2():
    var1 = var1 + 1 # 전역변수를 수정하려면  global이라는 키워드를 사용해야한다.
    print(var1)

vartest()

print(var1)

vartest2()