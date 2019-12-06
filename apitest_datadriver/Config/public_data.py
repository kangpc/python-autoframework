#encoding=utf-8
import os
# 整个项目的根目录绝对路径
baseDir = os.path.dirname(os.path.dirname(__file__))

# 设置数据文件的绝对路径
file_path = baseDir + r"/TestData/inter_test_data.xlsx"

'''inter_test_data.xlsx '''
# 2表示idx从2开始，即从sheet第七列第二行开始遍历,可理解为行号
idx_starting_from_2 = 2
# excel文件API sheet每行的单元格列号映射，以人脑思维方式，比如2表示第二列，3表示第三列
API_apiName = 2    # 接口名称
API_requestUrl = 3    # 接口请求url
API_requestMethod = 4    # 接口请求方法
API_paramsType = 5    # 接口参数类型
API_apiTestCaseFileName = 6    # 接口对测试用例sheet名称的映射
API_active = 7    # 接口是否执行标识

# 测试用例sheet单元格列号映射
CASE_requestData = 1    # 请求的数据
CASE_relyData = 2    # 请求依赖的上游相应数据
CASE_responseCode = 3    # 请求返回状态码
CASE_responseData = 4    # 请求相应内容
CASE_dataStore = 5    # 数据存储
CASE_checkPoint = 6    # 请求返回内容检查点
CASE_active = 7    # 用例是否执行标识
CASE_status = 8    # 用例执行结果状态
CASE_errorInfo = 9    # 用例执行结果错误信息

# 存储请求参数里面的依赖数据
REQUEST_DATA = {}

# 存储响应对象中的依赖数据
RESPONSE_DATA = {}



if __name__ == '__main__':
    print baseDir
    print file_path