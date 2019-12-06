# encoding=utf-8
import hashlib

def md5_encrypt(text):
    '''md5加密'''
    md5 = hashlib.md5()  # 把md5哈希对象加载到内存
    md5.update(text)  # 用字符串text更新md5对象(加密文本)
    return md5.hexdigest()  # 将md5对象加密后的摘要按十六进制的字符串形式返回

if __name__ == "__main__":
    print md5_encrypt("Aa20190106")
