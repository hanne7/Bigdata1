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
        
        vbar = "|"
        hyphen = "-"
        space = " "
        star = "*"
        
        space_num = int(n/2)
        star_num = 1
        hyphen_num = n

        while i < int(n/2)+1:
            print(space+hyphen*hyphen_num)
            while space_num>=0:
                print(vbar+space*space_num,end='')
                print(star*star_num,end='')
                print(space*space_num+vbar)
                space_num-=1
                star_num+=2
                i+=1
       
        space_num = 1
        star_num = n-2
        while i >= int(n/2)+1:
            while star_num>0:
                print(vbar+space*space_num,end='')
                print(star*star_num,end='')
                print(space*space_num+vbar)
                star_num-=2
                space_num +=1
                i+=1
            
            if i >= n:
                print(space+hyphen*hyphen_num)
                break
            
