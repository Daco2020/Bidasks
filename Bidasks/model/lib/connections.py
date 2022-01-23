import pymysql
from .config import DATABASE

class Connector():
    def __init__(self):
        self.db     = pymysql.connect(**DATABASE)
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    # 단일 인서트
    def execute(self, query, args={}):
        self.cursor.execute(query, args) 

    # 벌크 인서트(추가)
    def execute_many(self, query, args={}):
        self.cursor.executemany(query, args)         

    # 한번에 한 row
    def execute_one(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    # 모든 row
    def execute_all(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()




# # INSERT 함수 예제
# @test.route('/insert', methods=['GET'])
# def insert():
#     db_class= dbModule.Database()
 
#     sql     = "INSERT INTO testDB.testTable(test) \
#                 VALUES('%s')"% ('testData')
#     db_class.execute(sql)
#     db_class.commit()
 
#     return render_template('/test/test.html',
#                            result='insert is done!',
#                            resultData=None,
#                            resultUPDATE=None)
 
 
 
# # SELECT 함수 예제
# @test.route('/select', methods=['GET'])
# def select():
#     db_class= dbModule.Database()
 
#     sql     = "SELECT idx, test \
#                 FROM testDB.testTable"
#     row     = db_class.executeAll(sql)
 
#     print(row)
 
#     return render_template('/test/test.html',
#                             result=None,
#                             resultData=row[0],
#                             resultUPDATE=None)
 

# # UPDATE 함수 예제
# @test.route('/update', methods=['GET'])
# def update():
#     db_class= dbModule.Database()
 
#     sql     = "UPDATE testDB.testTable \
#                 SET test='%s' \
#                 WHERE test='testData'"% ('update_Data')
#     db_class.execute(sql)   
#     db_class.commit()
 
#     sql     = "SELECT idx, test \
#                 FROM testDB.testTable"
#     row     = db_class.executeAll(sql)
 
#     return render_template('/test/test.html',
#                             result=None,
#                             resultData=None,
#                             resultUPDATE=row[0])

# 출처: https://kkamikoon.tistory.com/entry/Python-Flask-웹-페이지-만들기-06-MySQL-연동하기DB-클래스-생성 [컴퓨터를 다루다]