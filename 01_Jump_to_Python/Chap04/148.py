def cal(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result+i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result*i
    elif choice == "sub":
        result = args[0]
        for i in args[1:]:
            result = result-i
    elif choice == "div":
        result = args[0]
        for i in args[1:]:
            result = result/i
    return result

print(cal('sum', 1,2,3,4,5))
print(cal('mul', 1,2,3,4,5))
print(cal('sub', 1,2,3,4,5))
print(cal('div', 1,2,3,4,5))
