# encoding:utf-8
import hashlib


def md5_encrypt(text):
	m5 = hashlib.md5()    # 构造md5对象，此时md5实例对象已加载到内存，要对一个新的对象用md5加密，需要构造新的md5，不然加密出来的数据会不对
	m5.update(text)    # 加密字符串text
	value = m5.hexdigest()    # 加密后获取加密字符串
	return value

if __name__ == '__main__':
	print md5_encrypt("Aa1111")
	print md5_encrypt("Aa2222")

