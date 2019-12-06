# encoding:utf-8
from utils.db_handler import DB
from utils.static_final import *
import sys
reload(sys)
sys.setdefaultencoding("utf8")


def new_file(apiInfo, api_case_list):  # apiInfo:tuple类型，interface_api表，每一行是一个tuple
    with open(script_path + "\\" + apiInfo[1] + "_test.py", "w") as fp:
        fp.write(code_head)
        if apiInfo[5] == 1:  # 表示需要连接数据库
            fp.write(class_head_db %(apiInfo[1].title(), apiInfo[0], apiInfo[2]))  # 字符串title方法：把字符串的首字母大写
        else:
            fp.write(class_head %(apiInfo[1].title(), apiInfo[0], apiInfo[2]))
        param_code = ""
        for idx, case in enumerate(api_case_list, 1):  # 使用索引号标注下第几条case
            if case[3]:  # rely_data有值，则需要做依赖数据处理
                # 获取依赖数据
                param_code = '''payload = self.dbd.param_completed(%s, %s)''' % (eval(case[2]), eval(case[3]))
            else:  # rely_data的值为空，则不需要处理依赖数据
                param_code = '''payload = %s''' % case[2]

            store_code = ""
            if case[6]:  # 对应interface_test_case表的data_store列
                # 需要写入存储依赖数据
                # case[2] if case[2] else None: case[2]就是interface_test_case表的r_data列，如果r_data有值，就返回值，如果为空，返回None
                store_code = '''self.dbd.store_data(%s, %s, %s, %s, %s)''' %(int(case[1]), int(case[0]), case[6],\
                                                                             case[2] if case[2] else None, "result") # result:是request
            if case[7]:  # case[7]对应存储规则，即interface_test_case表的data_store
                store_code += check_code %case[7]
            if apiInfo[3] == "post":
                fp.write(post_code %(apiInfo[1] + "_" + str(idx), str(idx), param_code, store_code))
            elif apiInfo[3] == "get":
                fp.write(get_code % (apiInfo[1] + "_" + str(idx), str(idx), param_code, store_code))
        if apiInfo[5] == 1:
            fp.write(class_end_db)
        fp.write(code_end)
        fp.close()


def create_script():
    db = DB()
    # 从数据库获取需要执行的api列表
    apiList = db.get_api_list()
    for api in apiList:  # api就是interface_api表的每一行，每一行是一个tuple
        # 根据api_id获取该接口的测试用例
        api_case_list = db.get_api_case(api[0])
        new_file(api[1:7], api_case_list)  # api_case_list是interface_test_case表的每一行

if __name__ == "__main__":
    create_script()

