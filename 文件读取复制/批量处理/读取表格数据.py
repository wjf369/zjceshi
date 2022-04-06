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
                    # mycursor.execute("UPDATE yourbay_tst.yb_tst_brain_activation_code  SET to_url = 'https://h5.yourbay.net/cmsh5/#/assessDirectorHome?jgid=%d',distributor_id=%d,status =2 WHERE type=2 AND qr_code =%d" % (can1,can1,bian3))
                    mydb.commit()
                    file = open('增加成功.txt', 'a', encoding='UTF-8')
                    file.write("\r\n")
                    file.write(str(bian3))
                    file.write("\r\n")
                    file.close()
                    print("空的，执行成功")
        else:
            print("结束,更新完毕")


data = xlrd.open_workbook("D:\\pythonProject\\文件读取复制\\批量处理\\新建 XLS 工作表.xls")
table = data.sheet_by_index(0)#通过索引获取，例如打开第一个sheet表格
# table2 = data.sheet_by_name("Sheet1")#通过名称获取，如读取sheet1表单
# names = data.sheet_names()    #返回book中所有工作表的名字
rows = table.nrows  #获取该sheet中的有效行数
# print(rows)

# table1 = table.row(2)  #返回由该行中所有的单元格对象组成的列表
# print(table1)
# t1 = table.row_slice(1)  #返回由该列中所有的单元格对象组成的列表
# print(t1)
#
# t = table.row_types(1, start_colx=0, end_colx=None)    #返回由该列中所有单元格的数据类型组成的列表array('B', [2, 2, 2])
# print(t)
#
# q = table.row_values(1, start_colx=0, end_colx=None)   #返回由该行中所有单元格的数据组成的列表[1607.0, 100005993.0, 100006000.0]
# print(q)

rows1=0
list1=[]
while rows1<rows:
    # print(rows1)
    list1.append(rows1)
    rows1 += 1
# print(list1) [0, 1, 2, 3, 4, 5]

# 1607	100005993	100005994
# 3202	100006010	100006012
# 3202	100006013	100006014
# 1607	100005995	100005996
# 1607	100005997	100006000


i = 0
while i < rows:
    # print(i)
    l =[0,1,2]
    for i in list1:
        print(i)
        zhi1 = table.cell_value(i,0)    #机构ID

        zhi2 = table.cell_value(i,1)    #开始编号

        zhi3 = table.cell_value(i,2)    #结束编号
        chuancan(zhi1, zhi2, zhi3)
        i += 1






