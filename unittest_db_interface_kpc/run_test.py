# encoding=utf-8
import time,sys
sys.path.append("./script")
from utils.HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
from interface.create_script import create_script
from utils.static_final import *
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
	# 生成测试脚本
	create_script()
	# 执行测试脚本
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	# 指定测试用例脚本的目录
	test_dir = base_dir + "\\script"
	# 在test_dir目录下找_test.py结尾的文件,加载组织成测试用例集合，赋给testsuit变量
	testsuit = defaultTestLoader.discover(test_dir, pattern="*_test.py")
	# 文件名和路径中不得含有反转字符，比如:<,>,:,",/,\,|,?,*
	filename = base_dir + "\\report\\" + now + "_result.html"
	# 打开按二进制写
	fp = open(filename, "wb")
	runner = HTMLTestRunner(stream=fp, title="接口自动化测试", description="接口自动化测试结果报告")
	runner.run(testsuit)
	fp.close()
