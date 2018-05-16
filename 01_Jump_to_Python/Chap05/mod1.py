def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a) != type(b):
        print("같은 타입이 아니기 때문에 더할 수 없습니다.")
        return
    else:
        result = sum(a,b)
    return  result

if __name__ == "__main__" :
    print(sum(1,2))
    print(safe_sum(1,2))
    print(safe_sum(1,'2'))