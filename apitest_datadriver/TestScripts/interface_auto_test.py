# coding:utf-8
import requests
import json
from Utils.ParseExcel import *
from Config.public_data import *
from Utils.HttpClient import *
from Action.get_rely import *
from Action.data_store import *
from Action.check_result import *
from Action.write_test_result import *

import sys
reload(sys)
sys.setdefaultencoding("utf-8")    # 设置了编码后，当前的编码都是utf-8,有中文显示不出来的问题可以尝试.decode("utf-8")

def main():
	pe = ParseExcel()
	pe.loadWorkBook(file_path)
	sheetObj = pe.getSheetByName(u"API")
	activeList = pe.getColumn(sheetObj, API_active)
	# 遍历api sheet，2表示idx从2开始，即从sheet第七列第二行开始遍历
	for api_idx, api_cell in enumerate(activeList[1:], idx_starting_from_2):
		# print idx, cell.value
		if api_cell.value.lower() == "y":
			# 第一步：读取需要执行的接口所在行的行对象
			api_rowObj = pe.getRow(sheetObj, api_idx)
			# for i in rowObj:
			# 	print i.value
			apiName = api_rowObj[API_apiName-1].value
			requestUrl = api_rowObj[API_requestUrl-1].value
			requestMethod = api_rowObj[API_requestMethod-1].value
			paramsType = api_rowObj[API_paramsType-1].value
			apiTestCaseFileName = api_rowObj[API_apiTestCaseFileName-1].value
			active = api_rowObj[API_active-1].value
			# 第二步: 读用例sheet表，准备执行测试用例
			caseSheetObj = pe.getSheetByName(apiTestCaseFileName)
			caseActiveObj = pe.getColumn(caseSheetObj, CASE_active)
			# 遍历测试用例sheet
			for case_idx, case_cell in enumerate(caseActiveObj[1:], idx_starting_from_2):
				if case_cell.value.lower() == "y":
					# 说明此case行需要执行
					case_rowObj = pe.getRow(caseSheetObj, case_idx)
					requestData = case_rowObj[CASE_requestData-1].value
					relyData = case_rowObj[CASE_relyData-1].value
					dataStore = case_rowObj[CASE_dataStore-1].value
					checkPoint = case_rowObj[CASE_checkPoint-1].value

					if relyData:
						# 发送接口请求之前，先做依赖数据的处理
						# getRelyData 有做eval处理（把字符串转成字典），不改底层的封装，
						# 所以这里需要用模板字符串再把getRelyData返回的字典类型数据转成字符串类型。
						requestData = "%s" % GetKey.getRelyData(eval(requestData), eval(relyData))
					# 拼接接口请求参数，发送接口请求
					httpC = HttpClient()
					response = httpC.request(requestMethod=requestMethod,
					              requestUrl=requestUrl,
					              paramsType=paramsType,
					              requestData=requestData
					)  # 发送完请求后再去存数据，把请求和相应对象的数据都存起来
					if response.status_code == 200:
						responseData = response.json()  # 把响应体（这里响应体为字典类型）转成json类型

						# 存储依赖数据
						if dataStore:  # 判断DataStore不为空，才调用
							RelyDataStore.do(eval(dataStore), apiName, case_idx-1, eval(requestData), responseData)
						# 比对结果
						errorKey = CheckResult.check(responseData, eval(checkPoint))
						print errorKey
						write_result(pe, caseSheetObj, responseData, errorKey, case_idx)
					else:
						print response.status_code

				else:
					print "用例被忽略执行！"



		else:
			print "接口被设置忽略执行!",

if __name__ == "__main__":
	main()


