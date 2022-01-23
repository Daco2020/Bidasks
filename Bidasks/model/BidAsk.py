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

    def select_one(code):
        db_class = Connector()
        sql = "SELECT * FROM bidasks WHERE code=(%s) ORDER BY created_at DESC LIMIT 1"
        rows = db_class.execute_all(sql, code)
        return rows

    def select_bulk(code):
        db_class = Connector()
        sql = "SELECT * FROM bidasks WHERE code=(%s) ORDER BY created_at DESC LIMIT 100"
        rows = db_class.execute_all(sql, code)
        return rows
