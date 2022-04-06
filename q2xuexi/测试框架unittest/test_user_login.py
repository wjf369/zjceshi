import unittest  # 导入unittest
import requests
import json
import mysql.connector

class TestUserLogin(unittest.TestCase):  # 类必须Test开头，继承TestCase才能识别为用例类


    def test_user_login_normal(self):  # 一条测试用例，必须test_开头
        mydb = mysql.connector.connect(
            host="rm-8vb6yntx7c0i3b51kbo.mysql.zhangbei.rds.aliyuncs.com",  # 数据库主机地址
            user="dev_wujinfa",  # 数据库用户名
            passwd="wjfuiop",  # 数据库密码
            database="yourbay"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT bind_token FROM yourbay.tp_nbv_userinfo where mobile ='18701635531'")
        rows2 = mycursor.fetchall()
        s = requests.session()  # 新建一个会话
        url = "https://api.yourbay.net/oms/user/loginUseToken"
        data = {
            "loginToken": rows2[0][0]
        }
        headers = {"Content-Type": "application/json"}  # 严格来说，我们需要在请求头里声明我们发送的格式
        res = s.post(url=url, json=data, headers=headers)  # JSON格式的请求，将数据赋给json参数
        print(res.text)  # {"code":0,"data":{"token":"at:C196D6AF3B93292AACFAC5FCEF69599FPABIJYOFMXZNURWFSHIGUAKTKKNQNDTQSMDNTG
        self.assertIn('"mobile":"18701635531"', res.text)  # 断言

    def test_user_login_password_wrong(self):
        mydb = mysql.connector.connect(
            host="rm-8vb6yntx7c0i3b51kbo.mysql.zhangbei.rds.aliyuncs.com",  # 数据库主机地址
            user="dev_wujinfa",  # 数据库用户名
            passwd="wjfuiop",  # 数据库密码
            database="yourbay"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT bind_token FROM yourbay.tp_nbv_userinfo where mobile ='18701635531'")
        rows2 = mycursor.fetchall()
        s = requests.session()  # 新建一个会话
        url = "https://api.yourbay.net/oms/user/loginUseToken"  # 获取用户的登录token
        data = {
            "loginToken": rows2[0][0]
        }
        headers = {"Content-Type": "application/json"}  # 严格来说，我们需要在请求头里声明我们发送的格式
        res = s.post(url=url, json=data, headers=headers)  # JSON格式的请求，将数据赋给json参数
        # print(res.text)  # {"code":0,"data":{"token":"at:C196D6AF3B93292AACFAC5FCEF69599FPABIJYOFMXZNURWFSHIGUAKTKKNQNDTQSMDNTG
        token = res.json().get("data").get("token")
        # print(token)  # at:C196D6AF3B93292AACFAC5FCEF69599FPABIJYOFMXZNURWFSHIGUAKTKKNQNDTQSMDNTGAFLCEFXNLDHZWRODZOHXNKCACPXZR623458FB5C5DC347440285S03V001
        url2 = "https://api.yourbay.net/oms/book/list"  # oms系统，书库，图书信息列表
        # orc_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access-token-v2={}'.format(token)
        data2 = {
            "feature": [],
            "page": 1,
            "pageSize": 10
        }
        headers = {"access-token-v2": token}
        res2 = s.post(url=url2, json=data2, headers=headers)
        # print(res2.text)  #{"code":0,"data":{"total":104143,"list":[{"bookId":49160,"title":"兔巴哥认读故事：全12册（京东专供）"
        self.assertIn('49160', res2.text)  # 断言


if __name__ == '__main__':  # 如果是直接从当前模块执行（非别的模块调用本模块）
    unittest.main(verbosity=2)  # 运行本测试类所有用例,verbosity为结果显示级别