import requests

res = requests.get("https://www.baidu.com")

# url: 字符串格式，参数也可以直接写到url中
# params：url参数，字典格式
# data: 请求数据，字典或字符串格式
# headers: 请求头，字典格式
# cookies: 字典格式，可以通过携带cookies绕过登录
# files: 字典格式，用于混合表单（form-data）中上传文件
# auth: Basic Auth授权，数组格式 auth=(user,password)
# timeout: 超时时间（防止请求一直没有响应，最长等待时间），数字格式，单位为秒
# print(res.status_code, res.reason) # 200 OK
# print(res.text) # 文本格式，有乱码
# print(res.content) # 二进制格式
# print(res.encoding) # 查看解码格式 ISO-8859-1
# print(res.apparent_encoding) # utf-8
# res.encoding='utf-8' # 手动设置解码格式为utf-8
# print(res.text) # 乱码问题被解决
# print(res.cookies.items()) # cookies中的所有的项 [('BDORZ', '27315')]
# print(res.cookies.get("BDORZ")) # 获取cookies中BDORZ所对应的值 27315
