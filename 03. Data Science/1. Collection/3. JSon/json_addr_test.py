import json

try:
    with open('ITT_Student.json',encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
except:
    json_big_data = []
    pass

jsonResult = json_big_data
learning_course_info_list = []

def learning_course_write():
    temp_learning_course_list=[]
    if (input("현재 수강 과목이 있습니까? (예: y/n): ") == 'y'):
        while True:
            temp_learning_course_list.append(
                {'close_date':input("종료일 (예: 2018-09-05): "),
                 'course_code':input("강의코드 (예: IB171106, OB0104 ..): "),
                 'course_name':input("강의명 (예: IOT 빅데이터 실무반): "),
                 'open_date':input("개강일 (예: 2017-11-06): "),
                 'teacher':input("강사 (예: 이현구): ")
                }
            )
            if(input("현재 수강하는 과목이 더 있습니까? (y/n)") == 'n'):
                break

    return  temp_learning_course_list

def search_student_all():
    student_list = []
    print()
    for student in jsonResult:
        student_list.append(student)

    if len(student_list) >= 2:
        print("복수 개의 결과가 검색되었습니다.")
        print(" ----- 요약 결과 -----")
        for student in student_list:
            print("학생 ID: %s, 학생 이름: %s" % (student['student_id'], student['student_name']))
        print()
    else:
        for student in student_list:
            print("* 학생 ID: %s" % student['student_id'])
            print("* 이름: %s" % student['student_name'])
            print("* 나이: %s" % student['student_age'])
            print("* 주소: %s" % student['address'])
            print("* 수강 정보")
            print(" + 과거 수강 횟수: %s" % student['total_course_info']['num_of_course_learned'])
            print(" + 현재 수강 과목")
            learning_course_info = student['total_course_info']['learning_course_info']

            if len(learning_course_info) >= 1:
                for i in learning_course_info:
                    print("  강의 코드: %s" % i['course_code'])
                    print("  강의명: %s" % i['course_name'])
                    print("  강사: %s" % i['teacher'])
                    print("  개강일: %s" % i['open_date'])
                    print("  종료일: %s" % i['close_date'])
                    print()
            else:
                print("현재 수강 중인 과목 없음")
                print()

def search_student(key):
    student_list = []
    search = input("검색어를 입력하세요: ")
    print()
    for student in jsonResult:
        if student[key].find(search) != -1:
            student_list.append(student)

    if len(student_list) >= 2:
        print("복수 개의 결과가 검색되었습니다.")
        print(" ----- 요약 결과 -----")
        for student in student_list:
            print("학생 ID: %s, 학생 이름: %s" % (student['student_id'], student['student_name']))
        print()
    elif len(student_list) == 0:
        print("존재하지 않는 자료입니다.")
    else:
        for student in student_list:
            print("* 학생 ID: %s" % student['student_id'])
            print("* 이름: %s" % student['student_name'])
            print("* 나이: %s" % student['student_age'])
            print("* 주소: %s" % student['address'])
            print("* 수강 정보")
            print(" + 과거 수강 횟수: %s" % student['total_course_info']['num_of_course_learned'])
            print(" + 현재 수강 과목")
            learning_course_info = student['total_course_info']['learning_course_info']

            if len(learning_course_info) >= 1:
                for i in learning_course_info:
                    print("  강의 코드: %s" % i['course_code'])
                    print("  강의명: %s" % i['course_name'])
                    print("  강사: %s" % i['teacher'])
                    print("  개강일: %s" % i['open_date'])
                    print("  종료일: %s" % i['close_date'])
                    print()
            else:
                print("현재 수강 중인 과목 없음")
                print()

def search_student2():
    student_list = []
    search = input("검색어를 입력하세요: ")
    print()
    for student in jsonResult:
        if student['total_course_info']['num_of_course_learned'].find(search) != -1:
            student_list.append(student)

    if len(student_list) >= 2:
        print("복수 개의 결과가 검색되었습니다.")
        print(" ----- 요약 결과 -----")
        for student in student_list:
            print("학생 ID: %s, 학생 이름: %s" % (student['student_id'], student['student_name']))
        print()
    else:
        for student in student_list:
            print("* 학생 ID: %s" % student['student_id'])
            print("* 이름: %s" % student['student_name'])
            print("* 나이: %s" % student['student_age'])
            print("* 주소: %s" % student['address'])
            print("* 수강 정보")
            print(" + 과거 수강 횟수: %s" % student['total_course_info']['num_of_course_learned'])
            print(" + 현재 수강 과목")
            learning_course_info = student['total_course_info']['learning_course_info']

            if len(learning_course_info) >= 1:
                for i in learning_course_info:
                    print("  강의 코드: %s" % i['course_code'])
                    print("  강의명: %s" % i['course_name'])
                    print("  강사: %s" % i['teacher'])
                    print("  개강일: %s" % i['open_date'])
                    print("  종료일: %s" % i['close_date'])
                    print()
            else:
                print("현재 수강 중인 과목 없음")
                print()

def search_student3():
    student_list = []
    print()
    for student in jsonResult:
        if len(student['total_course_info']['learning_course_info']) != 0:
            student_list.append(student)
    if len(student_list) >= 2:
        print("복수 개의 결과가 검색되었습니다.")
        print(" ----- 요약 결과 -----")
        for student in student_list:
            print("학생 ID: %s, 학생 이름: %s" % (student['student_id'], student['student_name']))
        print()
    else:
        print("* 학생 ID: %s" % student['student_id'])
        print("* 이름: %s" % student['student_name'])
        print("* 나이: %s" % student['student_age'])
        print("* 주소: %s" % student['address'])
        print("* 수강 정보")
        print(" + 과거 수강 횟수: %s" % student['total_course_info']['num_of_course_learned'])
        print(" + 현재 수강 과목")
        learning_course_info = student['total_course_info']['learning_course_info']

        if len(learning_course_info) >= 1:
            for i in learning_course_info:
                print("  강의 코드: %s" % i['course_code'])
                print("  강의명: %s" % i['course_name'])
                print("  강사: %s" % i['teacher'])
                print("  개강일: %s" % i['open_date'])
                print("  종료일: %s" % i['close_date'])
                print()
        else:
            print("현재 수강 중인 과목 없음")
            print()

def search_student4(key):
    student_list = []
    search = input("검색어를 입력하세요: ")
    print()
    for student in jsonResult:
        learning_course_info = student['total_course_info']['learning_course_info']
        for i in learning_course_info:
            if i[key].find(search) != -1:
                student_list.append(student)
    if len(student_list) >= 2:
        print("복수 개의 결과가 검색되었습니다.")
        print(" ----- 요약 결과 -----")
        for student in student_list:
            print("학생 ID: %s, 학생 이름: %s" % (student['student_id'], student['student_name']))
        print()
    elif len(student_list) == 1:
        print("* 학생 ID: %s" % student_list[0]['student_id'])
        print("* 이름: %s" % student_list[0]['student_name'])
        print("* 나이: %s" % student_list[0]['student_age'])
        print("* 주소: %s" % student_list[0]['address'])
        print("* 수강 정보")
        print(" + 과거 수강 횟수: %s" % student_list[0]['total_course_info']['num_of_course_learned'])
        print(" + 현재 수강 과목")
        if len(student_list[0]['total_course_info']['learning_course_info']) >= 1:
            for i in student_list[0]['total_course_info']['learning_course_info']:
                print("  강의 코드: %s" % i['course_code'])
                print("  강의명: %s" % i['course_name'])
                print("  강사: %s" % i['teacher'])
                print("  개강일: %s" % i['open_date'])
                print("  종료일: %s" % i['close_date'])
                print()
        else:
            print("현재 수강 중인 과목 없음")
            print()
    else:
        print("해당학생 없음")

def update_student(key):
    for student in jsonResult:
        if student['student_id'] == update_id:
            student[key] = input("변경할 값을 입력하세요: ")

def update_student2():
    for student in jsonResult:
        if student['student_id'] == update_id:
            student['total_course_info']['num_of_course_learned'] = input("변경할 값을 입력하세요: ")

def update_student3(key):
    for student in jsonResult:
        if student['student_id'] == update_id:
            if len(student['total_course_info']['learning_course_info']) == 1:
                student['total_course_info']['learning_course_info'][0][key] = input("변경할 값을 입력하세요: ")
            elif len(student['total_course_info']['learning_course_info']) >= 2:
                course_code_menu = input("현재 복수 과목을 수강중 입니다.\n 변경할 과목의 코드를 입력하세요: ")
                for course in student['total_course_info']['learning_course_info']:
                    if course['course_code'] == course_code_menu:
                        course[key] = input("변경할 값을 입력하세요: ")
            else:
                print("현재 수강중이 과목이 없습니다.")


# main
id_number = len(json_big_data)
while True:
    print("<<JSON기반 학생 정보 관리 프로그램>>")
    menu = input("""1. 학생 정보입력
2. 학생 정보조회
3. 학생 정보수정
4. 학생 정보삭제
5. 프로그램 종료
메뉴를 선택하세요: 
""")
    if menu == '1':
        id_number += 1
        student_id = 'ITT' + '%03d'%id_number
        jsonResult.append(
            {
                'address':input("주소 (예: 대구광역시 동구 아양로 135): "),
                'student_id':student_id,
                'student_age':input("나이 (예: 29): "),
                'student_name':input("이름 (예: 홍길동): "),
                'total_course_info':{
                    'learning_course_info':learning_course_write(),
                    'num_of_course_learned':input("과거 수강 횟수 (예: 1): ")
                }
            }
        )
    elif menu == '5':
        with open('ITT_Student.json', 'w', encoding='utf8') as outflie:
            readable_result = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
            outflie.write(readable_result)
            print('ITT_Student.json SAVED')
        print("학생 정보 관리 프로그램을 종료합니다.")
        break
    elif menu == '2':
        search_menu = input("""1. 전체 학생정보 조회
  검색 조건 선택
2. ID 검색
3. 이름 검색
4. 나이 검색
5. 주소 검색
6. 과거 수강 횟수 검색
7. 현재 강의를 수강중인 학생
8. 현재 수강 중인 강의명
9. 현재 수강 강사
10. 이전 메뉴
메뉴를 선택하세요: """)
        if search_menu == '3':
            search_student('student_name')
        elif search_menu == '1':
            search_student_all()
        elif search_menu == '2':
            search_student('student_id')
        elif search_menu == '5':
            search_student('address')
        elif search_menu == '4':
            search_student('student_age')
        elif search_menu =='6':
            search_student2()
        elif search_menu == '7':
            search_student3()
        elif search_menu == '8':
            search_student4('course_name')
        elif search_menu == '9':
            search_student4('teacher')
        else:
            print("이전 메뉴로 돌아갑니다.")
            print()
    elif menu == '3':
        st_lists = []
        update_id = input("수정할 학생 ID를 입력하세요: ")
        for student in jsonResult:
            if student['student_id'] == update_id:
                st_lists.append(student)
        if len(st_lists) == 0:
            print("ID가 존재하지 않습니다.\n")
            continue
        update_menu = input("""1. 학생 이름
2. 나이
3. 주소
4. 과거 수강횟수
5. 현재 수강 중인 강의 정보
0. 이전 메뉴
메뉴 번호를 입력하세요: """)
        if update_menu == '1':
            update_student('student_name')
        elif update_menu == '2':
            update_student('student_age')
        elif update_menu == '3':
            update_student('address')
        elif update_menu == '4':
            update_student2()
        elif update_menu == '5':
            update_learning_course_menu = input("""1.강의 코드
2. 강의명
3. 강사
4. 개강일
5. 종료일
0. 취소
메뉴 번호를 입력하세요: """)
            if update_learning_course_menu == '1':
                update_student3('course_code')
            elif update_learning_course_menu == '2':
                update_student3('course_name')
            elif update_learning_course_menu == '3':
                update_student3('teacher')
            elif update_learning_course_menu == '4':
                update_student3('open_date')
            elif update_learning_course_menu == '5':
                update_student3('close_date')
            else:
                print("초기 메뉴로 돌아갑니다")
    elif menu == '4':
        delete_id_menu = input("삭제할 학생 ID를 입력하세요: ")
        st_lists = []
        for student in jsonResult:
            if student['student_id'] == delete_id_menu:
                st_lists.append(student)
        if len(st_lists) == 0:
            print("ID가 존재하지 않습니다\n")
            continue
        delete_menu = input("""삭제 유형을 선택하세요.
1. 전체 삭제
2. 현재 수강 중인 특정 과목정보 삭제
3. 이전 메뉴
메뉴 번호를 선택하세요: """)
        if delete_menu == '1':
           i = 0
           while i < len(jsonResult):
               if jsonResult[i]['student_id'] == delete_id_menu:
                   del jsonResult[i]
                   print("학생정보가 삭제되었습니다.")
               i += 1
        elif delete_menu == '2':
            for student in jsonResult:
                if student['student_id'] == delete_id_menu:
                    if len(student['total_course_info']['learning_course_info']) == 0:
                        print("현재 수강중인 과목이 없습니다.")
                        print()
                    elif len(student['total_course_info']['learning_course_info']) == 1:
                        i = 0
                        while i < len(jsonResult):
                            if jsonResult[i]['student_id'] == delete_id_menu:
                                del jsonResult[i]['total_course_info']['learning_course_info'][0]
                                print("현재 수강중이던 과목 정보가 삭제되었습니다.")
                            i += 1
                    else:
                        del_course_menu = input("현재 복수 과목을 수강중입니다. 삭제할 과목 코드를 입력하세요: ")
                        for student in jsonResult:
                            if student['student_id'] == delete_id_menu:
                                i = 0
                                while i < len(student['total_course_info']['learning_course_info']):
                                    if student['total_course_info']['learning_course_info'][i]['course_code'] == del_course_menu:
                                            del student['total_course_info']['learning_course_info'][i]
                                    i += 1
                                print("현재 수강중이던 과목 정보가 삭제되었습니다.")
        else:
            print("이전메뉴로 돌아갑니다")



