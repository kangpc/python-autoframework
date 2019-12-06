#encoding=utf-8
import requests
import json
from Utils.ParseExcel import ParseExcel
from Config.public_data import *
from Utils.HttpClient import HttpClient
from Action.get_rely import GetKey
from Action.data_store import RelyDataStore

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def main():
    parseE = ParseExcel()
    parseE.loadWorkBook(file_path)
    sheetObj = parseE.getSheetByName(u"API")
    activeList = parseE.getColumn(sheetObj, API_active)
    for idx, cell in enumerate(activeList[1:], 2):
        if cell.value == "y":
            # 需要执行的接口所在行的行对象
            rowObj = parseE.getRow(sheetObj, idx)
            apiName = rowObj[API_apiName - 1].value
            requestUrl = rowObj[API_requestUrl - 1].value
            requestMethod = rowObj[API_requestMethod - 1].value
            paramsType = rowObj[API_paramsType - 1].value
            apiTestCaseFileName = rowObj[API_apiTestCaseFileName - 1].value

            # 下一步读用例sheet表，准备执行测试用例
            caseSheetObj = parseE.getSheetByName(apiTestCaseFileName)
            caseActiveObj = parseE.getColumn(caseSheetObj, CASE_active)
            for c_idx, col in enumerate(caseActiveObj[1:], 2):
                if col.value == "y":
                    # 说明此case行需要执行
                    caseRowObj = parseE.getRow(caseSheetObj, c_idx)
                    requestData = caseRowObj[CASE_requestData - 1].value
                    relyData = caseRowObj[CASE_relyData - 1].value
                    dataStore = caseRowObj[CASE_dataStore - 1].value
                    if relyData:
                        # 发送接口请求之前，先做依赖数据的处理
                        requestData = "%s" %GetKey.get(eval(requestData), eval(relyData))
                    # 拼接接口请求参数，发送接口请求
                    httpC = HttpClient()
                    print requestMethod, requestUrl, paramsType, requestData
                    response = httpC.request(requestMethod = requestMethod,
                                  requestUrl = requestUrl,
                                  paramsType = paramsType,
                                  requestData = requestData
                                  )
                    responseData = response.json()
                    # 存储依赖数据
                    if dataStore:
                        RelyDataStore.do(eval(dataStore),apiName, c_idx - 1, eval
(requestData),responseData)
                    # 比对结果



                else:
                    print "用例被忽略执行"
        else:
            print "接口被设置忽略执行"

if __name__ == '__main__':
    main()

