import sqlite3

def select_emp():
    conn = sqlite3.connect("c:/pydb/mydb.db")
    cur = conn.cursor()
    sql = "SELECT * FROM employee"  #db 검색
    cur.execute(sql)
    rs = cur.fetchall()     #모든 자료 가져오기
    # print(rs)
    for i in rs:
        print(i)

    conn.close()    #db 연결 종료 - 필수

def insert_emp():
    conn = sqlite3.connect("c:/pydb/mydb.db")   #db 연결 객체 생성
    cur = conn.cursor()
    sql = "INSERT INTO employee VALUES ('e1002', '손흥민', 30, 50000)" #data 추가
    cur.execute(sql)
    conn.commit()   #commit 실행 - 필수
    conn.close()

# insert_emp()
select_emp()