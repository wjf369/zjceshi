import json
import requests

import mysql.connector
import xlrd

mydb = mysql.connector.connect(
    host="rm-8vb6yntx7c0i3b51kbo.mysql.zhangbei.rds.aliyuncs.com",  # 数据库主机地址
    user="dev_wujinfa",  # 数据库用户名
    passwd="wjfuiop",  # 数据库密码
    database="yourbay"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT bind_token FROM yourbay.tp_nbv_userinfo where mobile ='18701635531'")
rows2 = mycursor.fetchall()
# print(rows2[0][0])   # 打印bind_token 16492143770QD589BAROA8ZFOP0YKQ54AUQED30FYH9N1UL3BVR

s = requests.session() # 新建一个会话

data = xlrd.open_workbook("D:\\pythonProject\\文件读取复制\\批量处理\\新建 XLS 工作表.xls")
table = data.sheet_by_index(0)#通过索引获取，例如打开第一个sheet表格
rows = table.nrows  #获取该sheet中的有效行数

url = "https://api.yourbay.net/oms/user/loginUseToken"  # 获取用户的登录token
data = {
    "loginToken":rows2[0][0]
}
headers = {"Content-Type":"application/json"} # 严格来说，我们需要在请求头里声明我们发送的格式
res = s.post(url=url, json=data, headers=headers) # JSON格式的请求，将数据赋给json参数
# print(res.text)  # {"code":0,"data":{"token":"at:C196D6AF3B93292AACFAC5FCEF69599FPABIJYOFMXZNURWFSHIGUAKTKKNQNDTQSMDNTG
token = res.json().get("data").get("token")
# print(token)  # at:C196D6AF3B93292AACFAC5FCEF69599FPABIJYOFMXZNURWFSHIGUAKTKKNQNDTQSMDNTGAFLCEFXNLDHZWRODZOHXNKCACPXZR623458FB5C5DC347440285S03V001
url2 = "https://api.yourbay.net/oms/book/list"   #oms系统，书库，图书信息列表
data2 ={
    "feature": [],
    "page": 1,
    "pageSize": 10
}
headers ={"access-token-v2":token}
res2 = s.post(url=url2,json=data2,headers=headers)
# print(res2.text)  #{"code":0,"data":{"total":104143,"list":[{"bookId":49160,"title":"兔巴哥认读故事：全12册（京东专供）"