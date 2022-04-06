#!usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="123456",  # 数据库密码
    database="test1"
)

mycursor = mydb.cursor()



mycursor.execute("SELECT book_id,title,cover_photo  FROM tp_lib_book_category WHERE cover_photo not  like ('%scdn.yourbay.net%') and  library_allocation=1")

rows = mycursor.fetchall()




# print(rows)
if len(rows) < 1 :
    print("空")
else:
    for rows1 in rows:
        bookid = rows1[0]
        url = rows1[2]

        print(url)
        mycursor.execute("")





#                     row = rows[0]
#                     mycursor.execute("UPDATE yourbay_tst.yb_tst_brain_activation_code  SET to_url = 'https://h5.yourbay.net/cmsh5/#/assessDirectorHome?jgid=%s',distributor_id=%d,status =2 WHERE type=2 AND qr_code =%d" % (row[0],row[0],bian3))
#                     mydb.commit()
#
#
#         else:
#             print("结束,更新完毕")
#
#
# chuancan('%涧西万国银座%','18701635531',100007000,100007002)