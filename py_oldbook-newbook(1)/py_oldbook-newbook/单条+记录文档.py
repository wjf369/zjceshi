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

def chuancan(can1,can2,can3,can4):

    mycursor.execute("SELECT res_id,contact_name,title,fudd FROM tp_nbv_res_jgmp WHERE title like '%s'  and flag=1 and  ownerby IN (SELECT uid FROM tp_nbv_userinfo WHERE mobile= '%s')" % (can1,can2))

    rows = mycursor.fetchall()
    # print(rows)
    if len(rows) < 1 :
        print(rows)
        print("空")
    elif len(rows) > 1 :
        print(rows)
        print("多")
    else:
        # print("输出当前需要修改的大脑激活码的跳转以及机构ID")
        leng=can4-can3
        while leng >= 0:
            bian3 = can3
            leng -= 1
            can3 += 1
            mycursor.execute("SELECT to_url,distributor_id from yourbay_tst.yb_tst_brain_activation_code WHERE qr_code = %d" % (bian3))
            rows1 = mycursor.fetchall()
            # print(rows1)
            for rows1 in rows1:
                if len(rows1[0]):
                    print("有数据了,通过其他方式查询，确认是否修改吧")
                    print(rows1)

                else:
                    print("空的，执行成功")
                    print(bian3)

                    row = rows[0]
                    mycursor.execute("UPDATE yourbay_tst.yb_tst_brain_activation_code  SET to_url = 'https://h5.yourbay.net/cmsh5/#/assessDirectorHome?jgid=%s',distributor_id=%d,status =2 WHERE type=2 AND qr_code =%d" % (row[0],row[0],bian3))
                    mydb.commit()


        else:
            print("结束,更新完毕")


chuancan('%涧西万国银座%','18701635531',100007000,100007002)