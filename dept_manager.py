from deptdb import *

def main():
    dept_dao = DeptDAO()

    while 1:
        selected_menu = display_menu()
        print('Selected Menu :', selected_menu) 

        match selected_menu:
            case 1:
                print('부서정보를 출력합니다.')
                dept_list = dept_dao.get_depts()
                for dept in dept_list:
                    print(dept['deptno'], dept['dname'], dept['loc'])
            case 2:
                print('부서정보를 입력을 시작합니다.')
                deptno = int(input('부서번호 입력 : '))
                dname = input('부서 이름 : ')
                loc = input('부서 위치 : ')
                print('입력된 데이터 :', deptno, dname, loc)
                print(dept_dao.insert_dept(deptno, dname, loc))

            case 3:
                print('부서정보를 수정을 시작합니다.')
                deptno = int(input('수정하고자하는 부서번호를 입력:'))
                dname = input('새로운 부서 이름:')
                loc = input('새로운 위치정보:')
                print('입력된 데이터 :', deptno, dname, loc)
                print(dept_dao.update_dept(deptno, dname, loc))

            case 4:
                print('부서정보를 삭제를 시작합니다.')
                deptno = int(input('삭제할 부서의 번호를 입력:'))
                print('입력 데이터', deptno)
                print(dept_dao.delete_dept(deptno))

            case 5:
                print('프로그램을 종료합니다.')
                return
            case _:
                print('메뉴 번호를 정확히 입력해주세요!')

    # 사용자가 메뉴번호를 입력
    # 1 => 리스트
    # 2 => 데이터 입력
    # 3 => 수정
    # 4 => 삭제
    # 5 => exit
# 사용자가 메뉴번호를 입력 입력된 번호 반환 함수
# 메뉴가 출력

def display_menu():
    menus = '''
    부서관리 프로그램
    --------------
    1. 부서 리스트
    2. 부서 정보 입력
    3. 부서 정보 수정
    4. 부서 정보 삭제
    5. 프로그램 종료
    메뉴 번호를 선택하세요!
    '''
    print(menus)
    num = int(input('메뉴를 입력하세요.'))
    return num


if __name__=='__main__':
    # print(DeptDAO().get_depts())
    main()