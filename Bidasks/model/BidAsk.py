from model.lib.connections import Connector


class BidAskModels:
    def insert(args):
        db_class = Connector()
        sql = """INSERT INTO bidasks(
            code, volume, bid, ask, created_at
            ) VALUES (
            %s, %s, %s, %s, %s)"""

        db_class.execute(sql, args)
        db_class.commit()
        return "Success"

    def insert_bulk(args):
        db_class = Connector()
        sql = """INSERT INTO bidasks(
            code, volume, bid, ask, created_at
            ) VALUES (
            %s, %s, %s, %s, %s)"""

        db_class.execute_many(sql, args)
        db_class.commit()
        return "Success"

    # 해당 종목 최근 호가 데이터 1개 반환
    def select_one(code):
        db_class = Connector()
        sql = "SELECT * FROM bidasks WHERE code=(%s) ORDER BY created_at DESC LIMIT 1"
        rows = db_class.execute_all(sql, code)
        return rows

    # 해당 종목 최근 호가 데이터 100개 반환
    def select_bulk(code):
        db_class = Connector()
        sql = "SELECT * FROM bidasks WHERE code=(%s) ORDER BY created_at DESC LIMIT 100"
        rows = db_class.execute_all(sql, code)
        return rows



#----
# args_all = list()

# def insert(args):
#     db_class = Connector()
#     sql      = """INSERT INTO bidasks(
#         code, volume, bid, ask, created_at
#         ) VALUES (
#         %s, %s, %s, %s, %s)"""

#     HandleBidAsk.args_all.append(args)
#     # print(len(HandleBidAsk.args_all)) # 콘솔 확인용
#     # print(HandleBidAsk.args_all) # 콘솔 확인용

#     # 100개 단위로 bulk insert
#     if len(HandleBidAsk.args_all) > 99:
#         db_class.execute_many(sql, HandleBidAsk.args_all)
#         db_class.commit()
#         HandleBidAsk.args_all.clear()
