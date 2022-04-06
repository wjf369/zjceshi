# 导入requests包
import requests

# # 1. 组装请求
# url = "https://postman-echo.com/headers"  # 这里只有url，字符串格式
# # 2. 发送请求，获取响应
# res = requests.get(url) # res即返回的响应对象
# # 3. 解析响应
# print(res.text)  # 输出响应的文本


# # 带参数的GET请求
# url = "https://postman-echo.com/get?test=123"  # 参数可以写到url里
# res = requests.get(url=url) # 第一个url指get方法的参数，第二个url指上一行我们定义的接口地址
# print(res.text)

# # 带参数的GET请求
# url = "http://www.tuling123.com/openapi/api"
# params = {"key":"ec961279f453459b9248f0aeb6600bbe","info":"你好"} # 字典格式，单独提出来，方便参数的添加修改等操作
# res = requests.get(url=url, params=params)
# print(res.text)


# # 传统表单类POST请求（x-www-form-urlencoded）
# url = "http://httpbin.org/post"
# data = {"name": "hanzhichao", "age": 18} # Post请求发送的数据，字典格式
# res = requests.post(url=url, data=data) # 这里使用post方法，参数和get方法一样
# print(res.text)


# # JSON类型的POST请求（application/json）
# url = "http://httpbin.org/post"
# data = '''{
#         "name": "hanzhichao",
#         "age": 18
#         }''' # 多行文本, 字符串格式，也可以单行（注意外层有引号，为字符串） data = '{"name": "hanzhichao", "age": 18}'
# res = requests.post(url=url, data=data) #  data支持字典或字符串
# print(res.text)


# import requests
import json # 使用到JSON中的方法，需要提前导入
#
# url = "http://httpbin.org/post"
# data = {
#         "name": "hanzhichao",
#         "age": 18
#         }  # 字典格式，方便添加
# headers = {"Content-Type":"application/json"} # 严格来说，我们需要在请求头里声明我们发送的格式
# res = requests.post(url=url, data=json.dumps(data), headers=headers) #  将字典格式的data变量转换为合法的JSON字符串传给post的data参数
# print(res.text)


# import requests
#
# url = "https://api.yourbay.net//mem/isTool"
# data = {"child_id": 421906}
# headers = {"Content-Type":"application/json","access-token-v2":"AT:5DA28D1F371BF246CD43FE91AC717DB0GSOVQVXG0BJX0BIXKISFBZV3VSDJOGYAVO4WOSNGMXJF9WR3ZJYHJKHW6UMXQRX9619F3C961F5A0321062861S01V003"} # 严格来说，我们需要在请求头里声明我们发送的格式
# res = requests.post(url=url, json=data, headers=headers) # JSON格式的请求，将数据赋给json参数
# # res = requests.post(url=url, data=json.dumps(data), headers=headers) #  将字典格式的data变量转换为合法的JSON字符串传给post的data参数
# print(res.text)

