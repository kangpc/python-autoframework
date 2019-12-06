# encoding:utf-8

# 取依赖数据

from Config.public_data import *
from Utils.md5_encrypt import *

REQUEST_DATA = {"用户注册":{"1":{"username":"2wcd","password":"sdfwe2"}}}
RESPONSE_DATA = {"用户注册":{"1":{"userid":1}},"login":{"1":{"token":"dsajkds"}}}


class GetKey(object):
	def __init__(self):
		pass

	# 这里使用类方法仅为了直接 类名.方法 调用简便，不需要再实例化类对象。
	# 该方法做数据依赖的处理，dataSource ->需要做处理的数据源（excel里的RequestData），relyData ->excel里的RelyData。
	# RelyData：存放的只是找到目标数据的路径，把存放在RelyData的取数据路径读出来，
	# 按照其规则拿到实际依赖的数据，再把数据存在真正的数据源dataSource，最终作为请求的参数拼接
	# relyData:{"request":{"username":"用户注册->1","password":"用户注册->1"}}

	'''举例：relyData={"request":{"username":"register->1","password":"register->1"}}
	#      dataSource={"username":"","password":""}
	#dataSource存储数据源，对应Excel表中登录sheet的RequestData；relyData是依赖数据
	#比如登录时需要用到注册时的用户名和密码，登录sheet里原始的dataSource格式是{"username":"","password":""}
	#调试代码演示了：dataSource原始格式，依赖数据的获取方式，
	# 通过request判断从REQUEST_DATA中获取数据，然后根据一步步切割出来的k和v就读到已经保存在REQUEST_DATA中的内容了'''
	@classmethod
	def getRelyData(self, dataSource, relyData):
		data = dataSource.copy()  # 数据源可能会被多次用到，所以这里先备份一份，使用不改变原数据源dataSource，因为对象都是内存地址
		for key, value in relyData.items():
			# Key="request"，value="username":"用户注册->1","password":"用户注册->1"
			if key == "request":  # 说明依赖的数据来源于REQUEST_DATA里面
				# 说明应该去REQUEST_DATA获取值
				# {"request":{"username":"用户注册->1","password":"用户注册->1"},"response":{"userid":"用户注册->1"}}
				for k, v in value.items():
					# k="username"和"password"，v="用户注册->1"
					interfaceName, case_id = v.split("->")
					# print interfaceName, type(interfaceName)
					# interfaceName=用户注册，case_id=1
					val = REQUEST_DATA[interfaceName][case_id][k]
					if k == "password":
						data[k] = md5_encrypt(val)
					else:
						data[k] = val
					# data[k] = RESPONSE_DATA[interfaceName.decode("utf-8")][case_id][k]
			elif key == "response":  # 说明依赖的数据来源于RESPONSE_DATA里面
				# 说明应该去RESPONSE_DATA获取值
				# {"用户注册":{"1":{"userid":1}},"用户登录":{"1":{"token":"dsajkds"}}}
				for k, v in value.items():
					interfaceName, case_id = v.split("->")
					# print interfaceName, type(interfaceName)
					data[k] = RESPONSE_DATA[interfaceName][case_id][k]
					# data[k] = RESPONSE_DATA[interfaceName.decode("utf-8")][case_id][k]
		return data  # 返回的是字典对象

if __name__ == '__main__':
	s = {"username":"","password":""}
	rely = {"request":{"username":"用户注册->1","password":"用户注册->1"}}
	print GetKey.getRelyData(s, rely)


