# encoding=utf-8
import MySQLdb
from utils.config_handler import ConfigParse
from datetime import datetime
from utils.Md5_encrypt import md5_encrypt


class DB_Data(object):
    def __init__(self):
        self.db_conf = ConfigParse().get_db_conf()
        self.conn = MySQLdb.connect(
            host=self.db_conf["host"],
            port=self.db_conf["port"],
            user=self.db_conf["user"],
            passwd=self.db_conf["password"],
            db=self.db_conf["db"],
            charset="utf8"
        )
        # 设置数据库变更自动提交
        self.conn.autocommit(1)
        self.cur = self.conn.cursor()

    def close_connect(self):
        # 关闭数据连接
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def get_rely_data(self, api_id, case_id):
        sqlStr = "select data_store from interface_data_store where api_id=%s and case_id=%s" %(api_id, case_id)
        self.cur.execute(sqlStr)
        # 字典对象
        rely_data = eval((self.cur.fetchall())[0][0])
        return rely_data

    # param对应interface_test_case表的r_data(原始数据)
    # rely_data对应interface_test_case表的rely_data，通过rely_data获取interface_data_store表的api_id和case_id来唯一确定data_store
    # 该函数实现：将data_store数据读出来set到param（复制一份param，不改变原值）
    def param_completed(self, param, rely_data):
        """处理依赖数据，使请求参数完整化"""
        paramSource = param.copy()
        for key, value in rely_data.items():
            api_id, case_id = key.split("->")
            relyData = self.get_rely_data(int(api_id), int(case_id))
            for k, v in relyData.items():
                if paramSource.has_key(k):
                    paramSource[k] = v
        return paramSource

    def has_rely_data(self, api_id, case_id):
        '''判断要插入的数据是否已经存在数据库'''
        sqlStr = "select data_store from interface_data_store where api_id=%s and case_id=%s" %(api_id, case_id)
        # 获取受影响的条数，0表示没有查到数据，>0表示至少有一条数据
        affect_num = self.cur.execute(sqlStr)
        # 返回受影响的条数
        return affect_num

    def in_store_data(self, api_id, case_id, storeData):
        '''向数据库写入依赖数据'''
        # 判断数据库中是否已存在这条数据
        has_data = self.has_rely_data(api_id, case_id)
        if has_data:
            # 数据库中已经存在这条数据，直接更新data_store字段即可
            sqlStr = "update interface_data_store set data_store=\"%s\", ctime=\"%s\" where api_id=%s and case_id=%s"
            # print storeData, datetime.now(), api_id, case_id # storeData，datetime.now()传进来不是字符串，需要加引号，也可以外面用单引号，就不用转义双引号了
            # sqlStr = 'update interface_data_store set data_store=\"%s\", ctime=\"%s\" where api_id=%s and case_id=%s'
            # sqlStr = "update interface_data_store set data_store='%s', ctime='%s' where api_id=%s and case_id=%s"
            self.cur.execute(sqlStr %(storeData, datetime.now(), api_id, case_id))
        else:
            # 数据库中不存在这条数据，需要添加
            sqlStr = "insert into interface_data_store value(%s, %s, \"%s\", \"%s\")"
            self.cur.execute(sqlStr %(api_id, case_id, storeData, datetime.now()))

    def store_data(self, api_id, case_id, storeReg, requestData = None, responseData = None):  # storeReg:存储规则,就是interface_test_case表的data_store
        """存储依赖数据"""
        storeData = {}
        for key, value in storeReg.items():  # value是list类型，可以看数据库
            if requestData and key == "request":   #从请求参数中取依赖数据
                for i in value:
                    if requestData.has_key(i):
                        if i == "password":
                            storeData[i] = md5_encrypt(requestData[i])
                        else:
                            storeData[i] = requestData[i]
            elif responseData and key == "response":   #从相应参数中取依赖数据
                for j in value:
                    if responseData.has_key(j):
                        if j == "password":
                            storeData[j] = md5_encrypt(responseData[j])
                        else:
                            storeData[j] = responseData[j]
        # 将依赖数据写入数据库
        self.in_store_data(api_id, case_id, storeData)


if __name__ == "__main__":
    dbd = DB_Data()
    # param = {"username": "srwcx01", "password": "wcx123wac1"}
    # rely_data = {"1->1": ["username"]}
    dbd.store_data(2, 2, {"request": ["userid", "token", "password"]}, {"userid": 111, "token": "dsakl12334", "password": "Aa1111"})

