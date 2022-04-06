#!usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector

mydb = mysql.connector.connect(
    host="39.98.169.249",  # 数据库主机地址
    user="dev_wujinfa",  # 数据库用户名
    passwd="wjfuiop",  # 数据库密码
    database="yourbay_test"
)

mycursor = mydb.cursor()

def chuancan2(can1,can2,can3,can4):

    mycursor.execute("SELECT res_id,contact_name,title,fudd FROM tp_nbv_res_jgmp WHERE title like '%s'  and flag=1 and  ownerby IN (SELECT uid FROM tp_nbv_userinfo WHERE mobile= '%s')" % (can1,can2))

    rows = mycursor.fetchall()
    print(rows)
    for row in rows:
        # mycursor.execute("UPDATE yb_tst_brain_activation_code  SET to_url = https://h5.yourbay.net/cmsh5/#/assessDirectorHome?jgid='%s',distributor_id='%s',status =2 WHERE type=2 AND qr_code >=%d AND qr_code <=%d" % (row(0),row(0),can3, can4))
        mycursor.execute("UPDATE yourbay_tst.yb_tst_brain_activation_code  SET to_url = 'https://h5.yourbay.net/cmsh5/#/assessDirectorHome?jgid=%s',distributor_id=%d,status =2 WHERE type=2 AND qr_code >=%d AND qr_code <=%d" % (row[0],row[0],can3, can4))
        mydb.commit()

chuancan2('%涧西万国银座%','18701635531',100007000,100007002)




