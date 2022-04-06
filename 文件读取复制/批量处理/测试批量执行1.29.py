import xlrd

import mysql.connector

mydb = mysql.connector.connect(
    host="39.98.169.249",  # 数据库主机地址
    user="dev_wujinfa",  # 数据库用户名
    passwd="wjfuiop",  # 数据库密码
    database="yourbay_test"
)
mycursor = mydb.cursor()


def chuancan(can1,can3,can4):

    mycursor.execute("SELECT * from tp_nbv_res_jgmp WHERE res_id in (%d)" % ( can1))
    rows2 = mycursor.fetchall()
    if can4 - can3 > 1001:
        print("超过1000条")
        print(can4 - can3)
        file = open('超过1000条.txt', 'a', encoding='UTF-8')
        file.write(str(can1))
        file.write("\r\n")
        file.close()
    elif rows2 == []:
        print("机构不存在")
        file = open('机构不存在.txt', 'a', encoding='UTF-8')
        file.write(str(can1))
        file.write("\r\n")
        file.close()
    else:
        print("输出当前需要修改的大脑激活码的跳转以及机构ID")
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
                    file = open('有数据了.txt', 'a', encoding='UTF-8')
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
                    print("执行成功")
        else:
            print("结束,更新完毕")


data = xlrd.open_workbook("D:\\pythonProject\\文件读取复制\\批量处理\\新建 XLS 工作表.xls")
table = data.sheet_by_index(0)#通过索引获取，例如打开第一个sheet表格
rows = table.nrows  #获取该sheet中的有效行数


rows1=0
list1=[]
while rows1<rows:
    list1.append(rows1)
    rows1 += 1

i = 0
while i < rows:
    l =[0,1,2]
    for i in list1:
        zhi1 = table.cell_value(i,0)    #机构ID
        zhi2 = table.cell_value(i,1)    #开始编号
        zhi3 = table.cell_value(i,2)    #结束编号
        chuancan(int(zhi1), int(zhi2), int(zhi3))
        i += 1


