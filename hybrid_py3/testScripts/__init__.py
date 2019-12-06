#encoding=utf-8

from action.PageAction import *
from utils.ParseExcel import ParseExcel
from config.VarConfig import *
import time
import traceback

# # 设置此次测试的环境编码为utf8
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

# 创建解析Excel对象
excelObj = ParseExcel()
# 将Excel数据文件加载到内存
excelObj.loadWorkBook(dataFilePath)
