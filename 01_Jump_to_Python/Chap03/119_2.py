# coding: cp949

card = input("ī�带 �����ϰ� �ֽ��ϱ�? (y/n): ")
partnership = input("��Ű���� �ý� �����Դϱ�? (y/n): ")
if card == 'y':    card = True
else:              card = False
if partnership == 'y':    partnership = True
else:              partnership = False

#if card == True:
#    if partnership == True:
#        print("�ýø� Ÿ�� ���� �� �ֽ��ϴ�.")
# 12�� ������ �����ϰ� ó���ǹǷ� ��ø��if�� ����� �ʿ䰡 ����

#if card and partnership == True: <-x ������ ������ �����ؾ���
if card == True and partnership == True:
    print("�ýø� Ÿ�� ���� �� �ֽ��ϴ�.")
else:
    print("�ɾ�ž� �մϴ�.") 