# coding: cp949

coffee_number = 10
menu = """
        <Menu>
        1. Ŀ�Ǳ���
        2. Ŀ���ܷ�Ȯ��
        3. ���α׷� ����
        �޴��� �����ϼ��� : """

while True:

    print(menu,end='')
    menu_number = int(input())

    if menu_number == 1:
        money = int(input("\n�ݾ��� �Է��ϼ���: "))
        if money == 300:
            print("Ŀ�Ǹ� �ݴϴ�.")
            coffee_number = coffee_number - 1
        elif money > 300:
            print("Ŀ�Ǹ� �ݴϴ�.\n���� �Ž����� %d�� �Դϴ�." % (money - 300))
            coffee_number = coffee_number - 1
        else :
            print("�ݾ��� ���ڶ��ϴ�.")

    elif menu_number == 2:
        print("���� Ŀ���� ���� %d�� �Դϴ�." % coffee_number)           
    elif menu_number == 3:
        print("���α׷��� �����մϴ�.\n")
        break    
    
    if not coffee_number:
        print("Ŀ�ǰ� �� ���������ϴ�. �ǸŸ� �����մϴ�.")
        break
