# encoding=utf-8
import requests
import json

class HttpClient(object):
    def __init__(self):
        pass

    def request(self, requestMethod, requestUrl, paramsType,
               requestData = None, headers = None, cookies = None):
        if requestMethod.lower() == "post":
            if paramsType == "form":
                # eval(requestData)把unicode字符串转成字典（excel读出来都是unicode字符串，除非excel里存的是数字），如：‘{}’-->{}
                response = self.__post(url = requestUrl, data = json.dumps(eval(requestData)),
                                       headers = headers, cookies = cookies)
                return response
            elif paramsType == "json":
                response = self.__post(url=requestUrl, json = json.dumps(eval(requestData)),
                                       headers = headers, cookies = cookies)
                return response
        elif requestMethod == "get":
            if paramsType == "url":
                request_url = "%s%s" %(requestUrl, requestData)
                response = self.__get(url = request_url,
                                       headers = headers, cookies = cookies)
                return response
            elif paramsType == "params":
                response = self.__get(url=requestUrl, params = requestData,
                                      headers=headers, cookies=cookies)
                return response

    def __post(self, url, data = None, json = None, **kwargs):
        response = requests.post(url = url, data = data, json = json)
        return response

    def __get(self, url, params = None, **kwargs):
        response = requests.get(url = url, params = params)
        return response

if __name__ == '__main__':
    hc = HttpClient()
    res = hc.request('post', 'http://39.106.41.11:8080/register/', 'form', '{"username":"srwcx01","password":"wcx123wac1","email":"wcx@qq.com"}')
    print res.json()
'''
    res = hc.request('get', 'http://www.baidu.com', 'url')
    print res.text()
仅支持restful这种api，不支持百度这种请求，百度相应回来的是一个页面
'''











