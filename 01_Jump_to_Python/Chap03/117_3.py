# coding: cp949

money = int(input("�󸶸� ���� �ֽ��ϱ�? "))
card = input("ī�带 �����ϰ� �ֽ��ϱ�? (y/n): ")
if card == 'y':    card = True
else:              card = False

if money >= 3000:
    print("�ýø� Ÿ�� ����")
else:
    if card == True:
#        print("�ýø� Ÿ�� ����") # ���� �ڵ� �ߺ�
        print("ī�� ���� �ý�. �ý� Ÿ�� ����") # �ߺ��ڵ� �ƴ� ��� ���
    print("�ɾ� ����")
