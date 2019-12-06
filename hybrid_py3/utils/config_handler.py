#encoding=utf-8

'''
从apiframe直接拷贝过来，未做对应修改
'''

import configparser
from utils.static_final import config_path

class ConfigParse(object):
    def __init__(self):
        self.cf = configparser.ConfigParser()

    def get_db_conf(self):
        self.cf.read(config_path)
        host = self.cf.get("mysqlconf", "host")
        port = self.cf.get("mysqlconf", "port")
        db = self.cf.get("mysqlconf", "db_name")
        user = self.cf.get("mysqlconf", "user")
        password = self.cf.get("mysqlconf", "password")
        return {"host":host,"port": int(port),"db":db,"user":user,"password":password}

if __name__ == "__main__":
    cp = ConfigParse()
    print(cp.get_db_conf())


