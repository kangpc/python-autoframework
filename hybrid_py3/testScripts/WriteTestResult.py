#encoding=utf-8
from . import *

'''
成功和失败的写入时间和结果，忽略不执行的清空原有的数据
'''

# 用例或用例步骤执行结束后，向excel中写执行结果信息
def writeTestResult(sheetObj, rowNo, colsNo, testResult,
                errorInfo = None, picPath = None):
    # 测试通过结果信息为绿色，失败为红色
    colorDict = {"pass":"green", "faild":"red", "":None}

    # 因为“测试用例”工作表和“用例步骤sheet表”中都有测试执行时间和
    # 测试结果列，定义此字典对象是为了区分具体应该写哪个工作表
    # 封装三类测试套件（suit）
    colsDict = {
        "testCase":[testCase_runTime, testCase_testResult],
        "caseStep":[testStep_runTime, testStep_testResult],
        "dataSheet":[dataSource_runTime, dataSource_result]}
    try:
        # 在测试步骤sheet中，写入测试结果，colsNo代表着
        # testCase,caseStep,dataSheet 三者之一,
        # colsNo指的是sheet类型，通过sheet类型找到要写哪一列（通过关联到字典的key找到列号）
        excelObj.writeCell(sheetObj, content = testResult,
                rowNo = rowNo, colsNo = colsDict[colsNo][1],
                style = colorDict[testResult])
        if testResult == "":
            # 清空时间单元格内容
            excelObj.writeCell(sheetObj, content = "",
                rowNo = rowNo, colsNo = colsDict[colsNo][0])
        else:
            # 在测试步骤sheet中，写入测试时间
            excelObj.writeCellCurrentTime(sheetObj,
                rowNo = rowNo, colsNo = colsDict[colsNo][0])
        if errorInfo and picPath:
            # 在测试步骤sheet中，写入异常信息
            excelObj.writeCell(sheetObj, content = errorInfo,
                    rowNo = rowNo, colsNo = testStep_errorInfo)
            # 在测试步骤sheet中，写入异常截图路径
            excelObj.writeCell(sheetObj, content = picPath,
                    rowNo = rowNo, colsNo = testStep_errorPic)
        else:
            if colsNo == "caseStep":
                # 在测试步骤sheet中，清空异常信息单元格
                excelObj.writeCell(sheetObj, content = "",
                        rowNo = rowNo, colsNo = testStep_errorInfo)
                # 在测试步骤sheet中，清空异常信息单元格
                excelObj.writeCell(sheetObj, content = "",
                        rowNo = rowNo, colsNo = testStep_errorPic)
    except Exception as e:
        print(u"写excel时发生异常")
        print(traceback.print_exc())


