# encoding=utf-8

import re

class CheckResult(object):
	def __init__(self):
		pass

	@classmethod
	def check(cls, responseObj, checkPoint):
		'''
		responseObj:相应体获取的实际结果
		checkPoint：事先写好的期望结果
		'''
		# 检查点：
			# 业务code（等价的去检测，直接用"00"），
			# userid（检查数据类型是int类型，即全是数字即可），
			# token（既有数字又有字母用正则）
		# 如果值是一个字典，就需要正则去比对，
		# 如果是一个字符串或者整型，就用等价比对
		{"code": "00", "userid": {"value": "\w+"}}
		errorKey = {}  # 不满足的写进来
		for key, value in checkPoint.items():
			if isinstance(value, (str, unicode)):
				# 说明是等值校验
				if responseObj[key] != value:
					errorKey[key] = responseObj[key]
			elif isinstance(value, dict):
				# 说明是字典类型
				sourceData = responseObj[key]  # 接口返回原始值
				if value.has_key("value"):
					# 说明是通过正则校验
					regStr = value["value"]
					rg = re.match(regStr, "%s" %sourceData)  # # regStr是pattern
					if not rg:
						errorKey[key] = sourceData
				elif value.has_key("type"):
					# 说明是校验数据类型，# type有可能是整型也可能是字符型
					typeS = value["type"]
					if typeS == "N":  # N表示是整型
						if not isinstance(sourceData,(int, long)):
							errorKey[key] = sourceData
		return errorKey

if __name__ == "__main__":
	res = {"code": "01", "userid": 12, "id": "asd"}
	che = {"code": "00", "userid": {"type": "N"}, "id": {"value": "\d+"}}
	print CheckResult.check(res, che)


