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

def chuancan(can1,can3,can4):

    if can4 - can3>1001 :
        print("超过1000条")
        print(can4 - can3)
    else:
        # print("输出当前需要修改的大脑激活码的跳转以及机构ID")
        leng=can4-can3
        # print(leng)
        while leng >= 0:
            bian3 = can3
            leng -= 1
            can3 += 1
            mycursor.execute("SELECT to_url,distributor_id,qr_code from yourbay_tst.yb_tst_brain_activation_code WHERE qr_code = %d" % (bian3))
            rows1 = mycursor.fetchall()
            # print(rows1)
            for row1 in rows1:
                if len(row1[0]):
                    print("有数据了,通过其他方式查询，确认是否修改吧")
                    file = open('已经存在.txt', 'a', encoding='UTF-8')
                    file.write(str(row1[0]))
                    file.write("\r\n")
                    file.close()
                    print(row1[0])
                else:
                    print(bian3)
                    # row = rows[0]
                    mycursor.execute("UPDATE yourbay_tst.yb_tst_brain_activation_code  SET to_url = 'https://h5.yourbay.net/cmsh5/#/assessDirectorHome?jgid=%d',distributor_id=%d,status =2 WHERE type=2 AND qr_code =%d" % (can1,can1,bian3))
                    mydb.commit()
                    file = open('增加成功.txt', 'a', encoding='UTF-8')
                    file.write("\r\n")
                    file.write(str(bian3))
                    file.write("\r\n")
                    file.close()
                    print("数据添加成功，执行成功")
        else:
            print("结束")

chuancan( 3977,100092001,100093000)