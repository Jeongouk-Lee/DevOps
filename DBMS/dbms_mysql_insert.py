import pymysql

# MySQL 서버 연결
conn = pymysql.connect(
    host="localhost",
    #port="3307"
    user='root',
    passwd='1234',
    database="exampledb",
    # charset="utf8mb4",
    # cursorclass=pymysql.cursors.DictCursor
)

# 커서 생성 => 명령어 작성
cursor = conn.cursor()

# 명령어 실행
sql ="""
insert into employees1(id, name, DeptID, ManagerID)
values(8,'kenneth',8,101);
"""
cursor.execute(sql)
conn.commit()
 
# 연결 해제
conn.close()