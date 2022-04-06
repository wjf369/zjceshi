import mysql.connector

mydb = mysql.connector.connect(
    host="39.98.169.249",  # 数据库主机地址
    user="dev_wujinfa",  # 数据库用户名
    passwd="wjfuiop",  # 数据库密码
    database="yourbay_test"
)
mycursor = mydb.cursor()
can1 = 3202
mycursor.execute("SELECT * from tp_nbv_res_jgmp WHERE res_id in (%d)" % ( can1))
rows2 = mycursor.fetchall()
print(rows2)
if rows2 == []:
    print("kongde ")
else:
    print("有")
