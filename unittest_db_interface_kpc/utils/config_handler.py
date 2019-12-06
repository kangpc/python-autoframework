#encoding=utf-8
import ConfigParser
from utils.static_final import config_path


# 该类解析配置文件
class ConfigParse(object):
    def __init__(self):
        self.cf = ConfigParser.ConfigParser()

    def get_db_conf(self):
        self.cf.read(config_path)
        host = self.cf.get("mysqlconf", "host")
        port = self.cf.get("mysqlconf", "port")
        db = self.cf.get("mysqlconf", "db_name")
        user = self.cf.get("mysqlconf", "user")
        password = self.cf.get("mysqlconf", "password")
        return {"host": host, "port": int(port), "db": db, "user": user, "password": password}

if __name__ == '__main__':
    cp = ConfigParse()
    cp.get_db_conf()