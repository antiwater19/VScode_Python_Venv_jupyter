import pymysql

# 데이터베이스 연결기능 클래스 => Connection
class DBConnect:

    @classmethod
    def get_db(self):
        return pymysql.connect(
            host='127.0.0.1',
            user='notroot',
            passwd='admin',
            db='dobyisfree',
            charset='utf8',
            autocommit=True # 빡빡하게 하면 자동 커밋할때 오류가 나는 경우가 있다.
        )
    



# 데이터베이스 CRUD  기능을 하는 클래스
class DeptDAO:
    # select
    def get_depts(self):
        # db connection -> Cursor
        try:
            conn = DBConnect.get_db()
            cursor = DBConnect.get_db().cursor()
            # sql 실행
            sql = 'select * from dept'
            cursor.execute(sql)
            # 결과 -> tuple
            rows = cursor.fetchall() # select 결과는 tuple
            ret = []  # 결과를 담을 리스트
            # 결과를 만들어서 반환 : dict => {'deptno': , 'dname': , 'loc':}
            for row in rows: 
                temp = {
                    'deptno': row[0],
                    'dname': row[1],
                    'loc': row[2]
                }
                ret.append(temp)

        except : 
            pass

        finally:
            if conn:
                 # db 연결 종료 이걸하지 않으면 db에 불화가 생기고 연결이 유지됨
                conn.close()

        return ret
        pass

    # insert
    def insert_dept(self, deptno, dname, loc):
        try:
            # Cursor
            conn = DBConnect.get_db()
            cusor = conn.cursor()
            # sql 실행
            sql = 'insert into dept (deptno, dname, loc) values (%s, %s, %s)'
            result_cnt = cusor.execute(sql, (deptno, dname, loc))
            # 결과 반환
            return f'insert OK : {result_cnt}'
        except :
            return 'insert_dept error'
        finally:
            if conn:
                conn.close()

    # update
    def update_dept(self, deptno, dname, loc):
        # Cursor
        try:
            conn = DBConnect.get_db()
            cusor = conn.cursor()

            # sql 실행
            sql = 'update dept set dname=%s, loc=%s where deptno=%s'
            cnt = cusor.execute(sql, (dname, loc, deptno))
            # 결과 반환
            return f'update OK : {cnt}'
        except:
            return 'update_dept error'
        finally:
            if conn:
                conn.close()

    # delete
    def delete_dept(self, deptno):
        
        try:
            # Cursor
            conn = DBConnect.get_db()
            cursor = conn.cursor()
            # sql 실행
            sql = 'delete from dept where deptno=%s'
            cnt = cursor.execute(sql, (deptno))
            # 결과 반환
            return f'delete OK : {cnt}'
        except:
            return 'delete_dept error'
        finally:
            if conn:
                conn.close()
        


if __name__ == '__main__':
    # db = DBConnect().get_db()
    db = DBConnect.get_db()
    print(db)
    # insert
    #print(DeptDAO().insert_dept(50, 'QA', 'JEJU'))

    # update
    #print(DeptDAO().update_dept(50, 'QA', 'JEJU'))

    #delete
    print(DeptDAO().delete_dept(50))

    print('-'*30)
    # select
    print(DeptDAO().get_depts())
