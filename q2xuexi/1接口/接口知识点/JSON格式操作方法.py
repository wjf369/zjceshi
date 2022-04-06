import json # 需要导入JSON包

# data = {'name': '张三', 'password': '123456', "male": True, "money": None} # 字典格式
# str_data = json.dumps(data) # 序列化，转化为合法的JSON文本（方便HTTP传输）
# print(str_data)   # 结果{"name": "\u5f20\u4e09", "password": "123456", "male": true, "money": null}


import requests
import json

res = requests.post("http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info=怎么又是你")
print(res.text) # 输出为一行文本
res_dict = res.json() # 将响应转为json对象（字典）等同于`json.loads(res.text)`
print(json.dumps(res_dict, indent=1, sort_keys=True, ensure_ascii=False)) # 重新转为文本

url = "http://httpbin.org/post"
data = {
        "name": "hanzhichao",
        "age": 18
        }  # 字典格式，方便添加
headers = {"Content-Type":"application/json"} # 严格来说，我们需要在请求头里声明我们发送的格式
res = requests.post(url=url, data=json.dumps(data), headers=headers) #  将字典格式的data变量转换为合法的JSON字符串传给post的data参数
print(res.text)