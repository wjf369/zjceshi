import json
import requests


s = requests.session() # 新建一个会话
url = "https://api.yourbay.net/oms/user/loginUseToken"
data = {
    "loginToken":"164888599244053746NPKM4KFOGCNH8B5XAQOVMPTHMFCX21E4GQ6KYNV"
}
headers = {"Content-Type":"application/json"} # 严格来说，我们需要在请求头里声明我们发送的格式
res = s.post(url=url, json=data, headers=headers) # JSON格式的请求，将数据赋给json参数
print(res.text)  # {"code":0,"data":{"token":"at:C196D6AF3B93292AACFAC5FCEF69599FPABIJYOFMXZNURWFSHIGUAKTKKNQNDTQSMDNTG

token = res.json().get("data").get("token")
print(token)  # at:C196D6AF3B93292AACFAC5FCEF69599FPABIJYOFMXZNURWFSHIGUAKTKKNQNDTQSMDNTGAFLCEFXNLDHZWRODZOHXNKCACPXZR623458FB5C5DC347440285S03V001
url2 = "https://api.yourbay.net/oms/book/list"
# orc_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access-token-v2={}'.format(token)
data2 ={
    "feature": [],
    "page": 1,
    "pageSize": 10
}
headers ={"access-token-v2":token}
res2 = s.post(url=url2,json=data2,headers=headers)
# print(res2.text)  #{"code":0,"data":{"total":104143,"list":[{"bookId":49160,"title":"兔巴哥认读故事：全12册（京东专供）"


res3 = s.get("https://api.yourbay.net/oms/user/getPermissions",headers=headers)
# print(res3.text)  #{"code":0,"data":{"menu":[{"name":"index","path":"/index","component":"Layout","redirect":"","meta":{"title":"首页"

res4 = s.get("https://api.yourbay.net/oms/plus/serverOrgList?searchKey=&type=1&page=1&pageSize=1000",headers=headers)
# print(res4.text)