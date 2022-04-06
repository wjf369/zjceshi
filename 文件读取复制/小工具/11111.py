#!usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector

mydb = mysql.connector.connect(
    host="rm-8vb6yntx7c0i3b51kbo.mysql.zhangbei.rds.aliyuncs.com",  # 数据库主机地址
    user="dev_wujinfa",  # 数据库用户名
    passwd="wjfuiop",  # 数据库密码
    database="yourbay"
)

mycursor = mydb.cursor()


mycursor.execute("SELECT jgid from tp_yb_jgmp_extention WHERE level =2")
rows1 = mycursor.fetchall()
for row1 in rows1:
    # print(row1[0])
    mycursor.execute("SELECT res_id,title from tp_nbv_res_jgmp WHERE flag = 1 and examine_flag =2 and res_id = %d" % (row1[0]))
    rows2 = mycursor.fetchall()
    # print(rows2)
    for row2 in rows2:
        # print(row2[0])
        mycursor.execute("SELECT jgid from tp_nbv_auth_jg2jg_access WHERE pjgid =  %d" % (row2[0]))
        rows3 = mycursor.fetchall()
        for row3 in rows3:
            mycursor.execute("SELECT level from tp_yb_jgmp_extention WHERE jgid = %d" % (row3[0]))
            rows4 = mycursor.fetchall()
            for row4 in rows4:
                if row4[0] == 3:
                    mycursor.execute("SELECT jgid from tp_nbv_auth_jg2jg_access WHERE pjgid =  %d" % (row4[0]))
                    rows5 = mycursor.fetchall()
                    for row5 in rows5:
                        print(row5[0])
                        mycursor.execute("SELECT count(*) from  tp_yb_borrowercard WHERE activedjgid =%d and flag =1 and endtime>'2021-7-6' " % (row5[0]))
                        rows6 = mycursor.fetchall()
                        # print(rows6)

                else:
                    mycursor.execute("SELECT count(*) from  tp_yb_borrowercard WHERE activedjgid =%d and flag =1 and endtime>'2021-7-6' " % (row4[0]))
                    # print(row4[0])
                    rows7 = mycursor.fetchall()
                    # print(rows7)






        # mycursor.execute("")



