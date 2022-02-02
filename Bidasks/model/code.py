from model.lib.connections import Connector


class CodeModels():
    def select_one(code):
        db_class = Connector()
        sql = "SELECT code FROM codes WHERE code=(%s)"
        row = db_class.execute_one(sql, code)
        return row

    def select_all():
        db_class = Connector()
        sql = "SELECT code FROM codes"
        rows = db_class.execute_all(sql)
        return rows

    def insert(code):
        db_class = Connector()
        sql = "INSERT IGNORE INTO codes (code) VALUES (%s)"
        db_class.execute(sql, code)
        db_class.commit()
        return True

    def delete(code):
        db_class = Connector()
        sql = "DELETE FROM codes WHERE code=(%s)"
        db_class.execute(sql, code)
        db_class.commit()
        return True
