# encoding:utf-8

import requests
import json

upData = {"username":"lily12",
	"password":"lily12323",
	"email":"lily@qq.com"
}

response = requests.post(url="http://39.106.41.11:8080/register/", data=json.dumps(upData))
print response.status_code
print response.json()
print response.text


