import mysql.connector

mydb = mysql.connector.connect(
    host="8vb6yntx7c0i3b51kbo.mysql.zhangbei.rds.aliyuncs.com",  # 数据库主机地址
    user="dev_wujinfa",  # 数据库用户名
    passwd="wjfuiop"  # 数据库密码
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)