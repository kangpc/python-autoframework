#encoding=utf-8
import unittest, requests
from interface.public_info import *
import os, sys,json

class Users_Login(unittest.TestCase):
    """用户登录"""
    def setUp(self):
        self.dbd = DB_Data()
        self.base_url = "http://39.106.41.11:8080/login/"

    def test_users_login_1(self):
        """1"""
        payload = self.dbd.param_completed({'username': 'kpc2019010606', 'password': 'Aa12345678'}, {'1->1': ['username', 'password']})
        r = requests.post(self.base_url, data = json.dumps(payload))
        result = r.json()
        self.assertEqual(r.status_code, 200)
        self.dbd.store_data(2, 2, {"response":["userid", "token","code"]}, {"username":"kpc2019010606","password":"Aa12345678"}, result)
        check_point = {"code": "00"}
        for key,value in check_point.items():
            self.assertEqual(result[key], value, msg = u"字段【{}】: expection: {}, reality: {}".format(key, value, result[key]))


    def tearDown(self):
        self.dbd.close_connect()

if __name__ == '__main__':
    unittest.main()
