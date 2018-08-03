import csv
import math

def get_csv_row_instance(primary_key):
    Row_instance=[]
    # 내용을 작성하세요.
    return Row_instance

def get_csv_col_instance(col_name):
    col_instance=[]
    col_index = data[0].index(col_name)
    for row in data[1:]:
        col_instance.append(row[col_index])
    return col_instance

def Convert_Type(col_instance):
    try:
        col_instance = list(map(int, col_instance))
    except ValueError:
        col_instance = list(map(float, col_instance))
    return col_instance

def My_Sum(data_list):
    My_Sum=0
    for i in data_list:
        My_Sum = My_Sum + i
    return My_Sum

def My_Average(data_list):
    My_Average=0
    for i in data_list:
        My_Average = My_Average + i
    My_Average = My_Average/len(data_list)
    return My_Average

def My_Max(data_list):
    My_Max=0
    for i in data_list:
        if My_Max < i:
            My_Max = i

    return My_Max

def My_Min(data_list):
    My_Min = 0
    for i in data_list:
        if My_Min > i:
            My_Min = i

    return My_Min

def My_Deviation(data_list):
    for i in data_list:
        print("%-5s"%i, end='  ')
        print("%10s"%(i - My_Average(data_list)))

def My_Standard_Deviation(data_list):# 표준편차
    Variance = My_Variance(data_list)
    My_Standard_Deviation = Variance**0.5

    return My_Standard_Deviation

def My_Variance(data_list):#분산
    My_Variance=0
    for i in data_list:
        My_Variance = My_Variance + (i-My_Average(data_list))**2
    My_Variance = My_Variance/len(data_list)

    return My_Variance

def My_Ascendant(data_list):#오름차순
    sorts = sorted(data_list)
    for i in sorts:
        print(i, end='  ')

def My_Descendant(data_list):#내림차순
    sorts = list(reversed(sorted(data_list)))
    for i in sorts:
        print(i, end='  ')

def print_row(row_instance):
    for row_element in row_instance:
        print(row_element)

def print_col(col_instance):
    for col_element in col_instance:
        print(col_element)

with open('Demographic_Statistics_By_Zip_Code.csv',newline='') as infile:
    data=list(csv.reader(infile))

# menu 처리
while True:
    menu = input("""<CSV Handle 연습예제>
0.종료 1.행 2.열 3.총합 4.평균 5.최댓값 6.최솟값 7.편차 8.표준편차 9.분산 10.오름차순정렬 11.내림차순정렬
메뉴를 선택하세요: """)

    if menu == '0':
        print("프로그램 종료합니다.")
        break
    else:
        access_key = input("Access Key를 입력하세요: ")
        if menu == "1":
            print_row(data[int(access_key) - 1])
            print()
        elif menu == "2":
            print_col(Convert_Type(get_csv_col_instance(access_key)))
            print()
        elif menu == "3":
            print_col(Convert_Type(get_csv_col_instance(access_key)))
            print("총합: ",end='')
            print(My_Sum(Convert_Type(get_csv_col_instance(access_key))))
            print()
        elif menu == "4":
            print_col(Convert_Type(get_csv_col_instance(access_key)))
            print("평균: ",end='')
            print(My_Average(Convert_Type(get_csv_col_instance(access_key))))
            print()
        elif menu == "5":
            print_col(Convert_Type(get_csv_col_instance(access_key)))
            print("최댓값: ",end='')
            print(My_Max(Convert_Type(get_csv_col_instance(access_key))))
            print()
        elif menu == "6":
            print_col(Convert_Type(get_csv_col_instance(access_key)))
            print("최솟값: ", end='')
            print(My_Min(Convert_Type(get_csv_col_instance(access_key))))
            print()
        elif menu == "7":
            print("편차(Deviation)공식 : 표본값 - 평균")
            print("표본 편차")
            data_list = Convert_Type(get_csv_col_instance(access_key))
            My_Deviation(data_list)
            print()
        elif menu == "8":
            print_col(Convert_Type(get_csv_col_instance(access_key)))
            print("표준편차(Standard Deviation) 공식 : √분산")
            print("표준편차 : %f"%My_Standard_Deviation(Convert_Type(get_csv_col_instance(access_key))))
            print()
        elif menu == "9":
            print_col(Convert_Type(get_csv_col_instance(access_key)))
            print("분산(Variance) 공식 : ∑(표본-평균)**2/표본수")
            print(My_Variance(Convert_Type(get_csv_col_instance(access_key))))
            print()
        elif menu == "10":
            My_Ascendant(Convert_Type(get_csv_col_instance(access_key)))
            print()
        elif menu == "11":
            My_Descendant(Convert_Type(get_csv_col_instance(access_key)))
            print()