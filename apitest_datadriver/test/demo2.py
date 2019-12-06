#encoding=utf-8

from Config.public_data import RESPONSE_DATA,REQUEST_DATA
# from utils.md5_encrypt import md5_encrypt

REQUEST_DATA={"register":{"1":{"username":"wangjing","password":"123456"}}}


#获取依赖数据
class GetKey(object):
    def __init__(self):
        pass
#举例：relyData={"request":{"username":"register->1","password":"register->1"}}
#      dataSource={"username":"","password":""}
#dataSource存储数据源，对应Excel表中登录sheet的RequestData；relyData是依赖数据
#比如登录时需要用到注册时的用户名和密码，登录sheet里原始的dataSource格式是{"username":"","password":""}
#调试代码演示了：dataSource原始格式，依赖数据的获取方式，
# 通过request判断从REQUEST_DATA中获取数据，然后根据一步步切割出来的k和v就读到已经保存在REQUEST_DATA中的内容了
    @classmethod
    def get(cls,dataSource,relyData):
        data=dataSource.copy()
        for Key,value in relyData.items():
            #Key="request"，value="username":"register->1","password":"register->1"
            if Key == "request":
                #说明从REQUEST_DATA中取数据
                for k,v in value.items():
                    #k="username"和"password"，v="register->1"
                    interfaceName,case_id = v.split("->")
                    #interfaceName=register，case_id=1
                    val=REQUEST_DATA[interfaceName][case_id][k]
                    if k == "password":
                        # data[k]=md5_encrypt(val)
                        pass
                    else:
                        data[k]=val
            elif Key == "response":
                #说明从RESPONSE_DATA中取数据
                interfaceName,case_id = v.split("->")
                data[k]=RESPONSE_DATA[interfaceName][case_id][k]
        return data

if __name__=="__main__":
    source={"username":"","password":""}
    rely={"request":{"username":"register->1","password":"register->1"}}
    print GetKey.get(source,rely)


