import requests
import re
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4)\
        AppleWebKit/537.36(KHTML, like Gecko) Chrome/52 .0.2743. 116 Safari/537.36'

    }  # 模拟浏览器访问
    response = requests.get(url, headers=headers)  # 请求访问网站
    html = response.text  # 获取网页源码
    return html  # 返回网页源码


soup = BeautifulSoup(get_html('https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&clk1=f6526d4329c38c97bdd168b58ca3eeff&keyword=%E5%9B%BE%E4%B9%A6&page=0'), 'lxml')  # 初始化BeautifulSoup库,并设置解析器
# print(get_html('https://www.jianshu.com/p/2f190ab5a869'))
# <html><head><script>window.location.href='https://passport.jd.com/uc/login'</script></head></html>
print(soup)
# s = soup.string

# print(s)
# result = re.search("window.location.href='(.*?)'", s, re.DOTALL)
# # print(result)
# if result:
#     print(result.group(1))
#     get = get_html(result.group(1))
#     be = BeautifulSoup(get, 'lxml')
#     # print(be)
#     for i in be.find_all(name='a'):
#         print(i.get_text())









# for div in soup.find_all(name='div'):  # 遍历父节点
#     print(div)
#     # for a in li.find_all(name='a'):  # 遍历子节点
#     #     if a.string == None:
#     #         pass
#     #     else:
#     #         print(a.string)  # 输出结果
#     for p in div.find_all(name='a'):
#         print(p.get_text())
