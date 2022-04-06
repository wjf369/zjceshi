import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="127.0.0.1",  # 数据库主机地址
#     user="root",  # 数据库用户名
#     passwd="123456",  # 数据库密码
#     database="test1"
# )
mydb = mysql.connector.connect(
    host="39.98.169.249",  # 数据库主机地址
    user="dev_wujinfa",  # 数据库用户名
    passwd="wjfuiop",  # 数据库密码
    database="yourbay_test"
)
# conn = pymysql.connect(host='39.98.169.249',port=3306,user='dev_wujinfa',passwd='wjfuiop',db='yourbay_test',charset='utf8')#测试库地址

mycursor = mydb.cursor()

# print(mycursor)

def chuancan(can3,can4):

    # mycursor.execute("SELECT age FROM user2  WHERE id=%s" % (canshu))
    # mycursor.execute("SELECT * FROM `tp_nbv_userinfo` WHERE mobile=18790998878")
    # mycursor.execute("SELECT res_id,contact_name,title,fudd FROM tp_nbv_res_jgmp WHERE title like '%唐山友谊天地%' and flag=1 and  ownerby IN (SELECT uid FROM tp_nbv_userinfo WHERE mobile='18701635531')")
    # mycursor.execute('SELECT res_id,contact_name,title,fudd FROM tp_nbv_res_jgmp WHERE title like % %s % and  ownerby IN (SELECT uid FROM tp_nbv_userinfo WHERE mobile=%s)'' % (can1,can2))
    # mycursor.execute("SELECT res_id,contact_name,title,fudd FROM tp_nbv_res_jgmp WHERE title like '%s'  and flag=1 and  ownerby IN (SELECT uid FROM tp_nbv_userinfo WHERE mobile= '%s')" % (can1,can2))
    # mycursor.execute("UPDATE yb_tst_brain_activation_code  SET to_url = 'https://h5.yourbay.net/cmsh5/#/assessDirectorHome?jgid=7522',distributor_id=7522,`status`=2
    # WHERE type=2 AND qr_code >=100043086 AND qr_code <=100043090;")
    mycursor.execute("UPDATE yourbay_tst.yb_tst_brain_activation_code  SET to_url = 'https://h5.yourbay.net/cmsh5/#/assessDirectorHome?jgid=1',distributor_id=1,status =2 WHERE type=2 AND qr_code >=%d AND qr_code <=%d" % (can3, can4))
    mydb.commit()
    # rows = mycursor.fetchall()
    # print(rows)
    # for row in rows:
    #     print(row)



chuancan(100007000,100007002)
