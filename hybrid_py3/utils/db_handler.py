#encoding=utf-8

'''
从apiframe直接拷贝过来，未做对应修改
'''

import MySQLdb
from .config_handler import ConfigParse

class DB(object):
    def __init__(self):
        self.db_conf = ConfigParse().get_db_conf()
        self.conn = MySQLdb.connect(
            host = self.db_conf["host"],
            port = self.db_conf["port"],
            user = self.db_conf["user"],
            passwd = self.db_conf["password"],
            db = self.db_conf["db"],
            charset = "utf8"
        )
        self.cur = self.conn.cursor()

    def close_connect(self):
        # 关闭数据连接
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def get_api_list(self):
        sqlStr = "select * from interface_api where status=1"
        self.cur.execute(sqlStr)
        # 返回tuple对象
        apiList = list(self.cur.fetchall())
        return apiList

    def get_api_case(self, api_id):
        sqlStr = "select * from interface_test_case where api_id=%s" %api_id
        self.cur.execute(sqlStr)
        api_case_list = list(self.cur.fetchall())
        return api_case_list

    def get_rely_data(self, api_id, case_id):
        sqlStr = "select data_store from interface_data_store where api_id=%s and case_id=%s" %(api_id, case_id)
        self.cur.execute(sqlStr)
        # 字典对象
        rely_data = eval((self.cur.fetchall())[0][0])
        return rely_data

if __name__ == '__main__':
    db = DB()
    print(db.get_api_list())
    print(db.get_rely_data(1,1))
