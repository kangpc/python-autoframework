#encoding=utf-8
import os

ieDriverFilePath = "D:\Python37\IEDriverServer"
chromeDriverFilePath = "D:\Python37\chromedriver"
# firefoxDriverFilePath = "e:\python27\geckodriver"

# 获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 异常图片存放目录
screenPicturesDir = parentDirPath + "\\exceptionpictures\\"

# 测试数据文件存放绝对路径
dataFilePath = parentDirPath + u"\\testData\\126邮箱创建联系人并发邮件.xlsx"

# 测试数据文件中，测试用例表中部分列对应的数字序号
testCase_testCaseName = 1
testCase_frameWorkName = 3
testCase_testStepSheetName = 4
testCase_dataSourceSheetName = 5
testCase_isExecute = 6
testCase_runTime = 7
testCase_testResult = 8

# 用例步骤表中，部分列对应的数字序号
testStep_testStepDescribe = 1
testStep_keyWords = 2
testStep_locationType = 3
testStep_locatorExpression = 4
testStep_operateValue = 5
testStep_runTime = 6
testStep_testResult = 7
testStep_errorInfo = 8
testStep_errorPic = 9

# 数据源表中，是否执行列对应的数字编号
dataSource_isExecute = 6
dataSource_email = 2
dataSource_runTime = 7
dataSource_result = 8

'''
测试用例
联系人：源数据
登录，发邮件，创建联系人：关键字
'''

