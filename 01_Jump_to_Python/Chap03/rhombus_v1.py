# coding: cp949
print("rhombus_v1")
while True:
    n = int(input("�غ� Ȧ���� �Է��ϼ���(0 <- ����) : "))
    if n==0:
        print("���α׷� ����")
        break
    elif n%2==0:
        print("¦���� �Է��������ʽÿ�.")
        print('')
    else:
        i=0
        space = " "
        star = "*"
        space_num = int(n/2)
        star_num = 1
        while i < int(n/2)+1:
            while space_num>=0:
                print(space*space_num,end='')
                print(star*star_num)
                space_num-=1
                star_num+=2
                i+=1
