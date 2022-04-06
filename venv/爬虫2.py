import requests
import re
from bs4 import BeautifulSoup


# def get_html(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4)\
#         AppleWebKit/537.36(KHTML, like Gecko) Chrome/52 .0.2743. 116 Safari/537.36'
#
#     }  # 模拟浏览器访问
#     response = requests.get(url, headers=headers)  # 请求访问网站
#     html = response.text  # 获取网页源码
#     return html  # 返回网页源码

file1 = open('./ces.html','rb')
html1= file1.read()

bs = BeautifulSoup(html1, 'html.parser')  # 初始化BeautifulSoup库,并设置解析器


# print(bs.prettify()) # 格式化html结构
# print(bs.title) # 获取title标签的名称
# print(bs.title.name) # 获取title的name
# print(bs.title.string) # 获取head标签的所有内容
# print(bs.head)
# print(bs.div)  # 获取第一个div标签中的所有内容
# print(bs.div["id"]) # 获取第一个div标签的id的值
# print(bs.a)
# print(bs.find_all("a")) # 获取所有的a标签
# print(bs.find(id="u1")) # 获取id="u1"


for item in bs.find_all("a"):
    print(item.get_text())




# for div in soup.find_all(class='bottom'):  # 遍历父节点
#     for a in li.find_all(name='a'):  # 遍历子节点
#         if a.string == None:
#             pass
#         else:
#             print(a.string)  # 输出结果
#     for p in div.find_all(name='a'):
#         if p.string == None:
#             pass
#         else:
#             print(p.string)

