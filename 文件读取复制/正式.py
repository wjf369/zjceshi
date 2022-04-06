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


# mycursor.execute("SELECT res_id,contact_name,title,fudd FROM yourbay.tp_nbv_res_jgmp WHERE title like '%手机端测试%' and flag=1 and  ownerby IN (SELECT uid FROM yourbay.tp_nbv_userinfo WHERE mobile='18701635531')")
# ro1 = mycursor.fetchall()
# print(ro1)
#
def chuancan(can1,can2,can3,can4):

    mycursor.execute("SELECT res_id,contact_name,title,fudd FROM tp_nbv_res_jgmp WHERE title like '%s'  and flag=1 and examine_flag=2 and  ownerby IN (SELECT uid FROM tp_nbv_userinfo WHERE mobile= '%s')" % (can1,can2))

    rows = mycursor.fetchall()
    # print(rows)
    if len(rows) < 1 :
        print(rows)
        print("空")
    elif len(rows) > 1 :
        print(rows)
        print("多")
    elif can4 - can3>1050 :
        print("超过1000条")
        print(can4 - can3)
    else:
        # print("输出当前需要修改的大脑激活码的跳转以及机构ID")
        leng=can4-can3
        while leng >= 0:
            bian3 = can3
            leng -= 1
            can3 += 1
            mycursor.execute("SELECT to_url,distributor_id,qr_code from yourbay_tst.yb_tst_brain_activation_code WHERE qr_code = %d" % (bian3))
            rows1 = mycursor.fetchall()
            # print(rows1)
            for rows1 in rows1:
                if len(rows1[0]):
                    print("有数据了,通过其他方式查询，确认是否修改吧")
                    file = open('已经存在121.txt', 'a', encoding='UTF-8')
                    file.write(str(rows1))
                    file.write("\r\n")
                    file.close()
                    # print(str(rows1))

                else:
                    print("空的，执行成功")
                    print(bian3)

                    row = rows[0]
                    mycursor.execute("UPDATE yourbay_tst.yb_tst_brain_activation_code  SET to_url = 'https://h5.yourbay.net/cmsh5/#/assessDirectorHome?jgid=%s',distributor_id=%d,status =2 WHERE type=2 AND qr_code =%d" % (row[0],row[0],bian3))
                    mydb.commit()
                    file = open('增加成功126.txt', 'a', encoding='UTF-8')
                    file.write(str(row))
                    file.write(str(bian3))
                    file.write("\r\n")
                    file.close()

        else:
            print("结束,更新完毕")
            print(rows)


chuancan('%东城美吉姆%','13509020199',100060001,100060500)


