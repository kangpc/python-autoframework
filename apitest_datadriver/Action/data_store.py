# encoding:utf-8

# 存数据

from Config.public_data import *


class RelyDataStore(object):
	def __init__(cls):
		pass

	# request_source：就是excel存的RequestData的数据
	@classmethod
	def do(cls, storePoint, apiName, caseId, request_source={}, response_source={}):  # 前三个因为不是命名参数，所以传参的时候参数位置一定要对应上
		print storePoint, apiName, caseId, request_source, response_source
		'''
		def do(cls, request_source, response_source， storePoint, apiName, caseId)：
		假如request_source, response_source不从请求参数或者响应体中获取，那这两个参数就不是必传，
		这样写就会有问题，所以需要改成命名参数给两个初始值'''
		# storePoint就是excel存的DataStore的数据，
		# storePoint结构如：
		# REQUEST_DATA = {"用户注册":{"1":{"username":"2wcd","password":"sdfwe2"}}}
		for key, value in storePoint.items():
			# key="request"和"response"，value=['username', 'password']和['userid']
			if key == "request":
				# 说明存储的数据来自请求参数，此时从request_source读取，传进来是字典对象
				["username","password"]
				for i in value:
					# 如果存在，说明['username', 'password']在数据源能找到
					# 如果不存在，可能是excel中找数据源的规则写的有问题
					if request_source.has_key(i):
						# 要看RESPONSE_DATA中是否存在apiName，caseId这两个key，如果存在，直接往里写
						'''每次要写value都要先判断key是否存在，每个value都是字典'''
						# 如果不存在，我们需要把结构给写出来，告诉变量REQUEST_DATA里面存的一个结构
						if not REQUEST_DATA.has_key(apiName):  # 一开始字典是空的，会先执行下面的语句块，写入apiName的value（是一个字典）
							# 说明有存储数据的结构还未生成，需要指明数据存储结构
							REQUEST_DATA[apiName] = {str(caseId): {i: request_source[i]}}  # 这就画出来了：外面一层字典，里面嵌套一层字典
						else:  # for第二次会走这里
							# 说明存储数据结构中最外层结构完整，比如注册接口的json，即apiName'注册接口'这层存在
							# 再判断接口名里面一层是否存在caseId,
							# 如果存在，把value存进去
							# 判断REQUEST_DATA就会有caseId（因为上次已经写进去了），执行下面的语句块
							if REQUEST_DATA[apiName].has_key(str(caseId)):
								REQUEST_DATA[apiName][str(caseId)][i] = request_source[i]
							# 如果不存在，我们需要把结构给写出来，告诉变量RESPONSE_DATA里面存的一个结构
							else:
								REQUEST_DATA[apiName][str(caseId)] = {i: request_source[i]}
					# 源数据不存在这个key，给一个提示
					else:
						print "请求参数中不存在字段" + i
			elif key == "response":
				# 说明存储的数据来自相应body
				["username","password"]
				for j in value:
					# 如果存在，说明['userjd']在数据源能找到
					# 如果不存在，可能是excel中找数据源的规则写的有问题
					if response_source.has_key(j):
						# 要看RESPONSE_DATA中是否存在apiName，caseId这两个key，如果存在，直接往里写
						'''每次要写value都要先判断key是否存在，每个value都是字典'''
						# 如果不存在，我们需要把结构给写出来，告诉变量RESPONSE_DATA里面存的一个结构
						if not RESPONSE_DATA.has_key(apiName):  # 一开始字典是空的，会先执行下面的语句块，写入apiName的value（是一个字典）
							# 说明有存储数据的结构还未生成，需要指明数据存储结构
							RESPONSE_DATA[apiName] = {str(caseId): {j: response_source[j]}}  # 这就画出来了：外面一层字典，里面嵌套一层字典
						else:  # for第二次会走这里
							# 说明存储数据结构中最外层结构完整，比如注册接口的json，即apiName'注册接口'这层存在
							# 再判断接口名里面一层是否存在caseId,
							# 如果存在，把value存进去
							# 判断RESPONSE_DATA就会有caseId（因为上次已经写进去了），执行下面的语句块
							if RESPONSE_DATA[apiName].has_key(str(caseId)):
								RESPONSE_DATA[apiName][str(caseId)][j] = response_source[j]
							# 如果不存在，我们需要把结构给写出来，告诉变量RESPONSE_DATA里面存的一个结构
							else:
								RESPONSE_DATA[apiName][str(caseId)] = {j: response_source[j]}
					# 源数据不存在这个key，给一个提示
					else:
						print "相应body中不存在字段" + j


if __name__ == '__main__':
	# req_s = {"username":"srwcx01","password":"wcx123wac1","email":"wcx@qq.com"}
	# sto_p = {"request": ["username","password"], "response":["userid"]}
	# res_s = {"username": "srwcx01", "code": "00"}
	# # RelyDataStore.do(req_s, req_s, sto_p, u"用户注册", 1)
	# RelyDataStore.do(req_s, {}, sto_p, "response")
	# print REQUEST_DATA
	# print RESPONSE_DATA
	r = {"username":"srwcx01","password":"wcx123wac1","email":"wcx@qq.com"}
	s = {"request":["username","password"],"response":["userid"]}
	res = {"userid":12,"code":"00"}
	RelyDataStore.do(s, "register", 1, r, res)
	print REQUEST_DATA
	print RESPONSE_DATA
















