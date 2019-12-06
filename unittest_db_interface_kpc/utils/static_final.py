# encoding=utf-8
import os

# 工程的根目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据库配置文件绝对路径
config_path = base_dir + "/config/db_config.ini"

# 测试脚本文件存放目录
script_path = base_dir + "/script"


code_head = '''#encoding=utf-8
import unittest, requests
from interface.public_info import *
import os, sys,json
'''

# 无数据库链接时
class_head = '''
class %s(unittest.TestCase):
    """%s"""
    def setUp(self):
        self.base_url = "%s"
'''

# 有数据库链接时
class_head_db = '''
class %s(unittest.TestCase):
    """%s"""
    def setUp(self):
        self.dbd = DB_Data()
        self.base_url = "%s"
'''

class_end_db = '''
    def tearDown(self):
        self.dbd.close_connect()
'''

code_end = '''
if __name__ == '__main__':
    unittest.main()
'''

post_code = '''
    def test_%s(self):
        """%s"""
        %s
        r = requests.post(self.base_url, data = json.dumps(payload))
        result = r.json()
        self.assertEqual(r.status_code, 200)
        %s
'''

get_code = '''\n
    def test_%s(self):
        """%s"""
        %s
        r = requests.get(self.base_url + str(payload))
        result = r.json()
        self.assertEqual(r.status_code, 200)
        %s
'''

check_code = '''
        check_point = %s
        for key,value in check_point.items():
            self.assertEqual(result[key], value, msg = u"字段【{}】: expection: {}, reality: {}".format(key, value, result[key]))
'''