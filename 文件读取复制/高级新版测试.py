import mysql.connector


class MysqlUtils:
    def __init__(self):
        self.mydb = mysql.connector.connect(
                    host="39.98.169.249",  # 数据库主机地址
                    user="dev_wujinfa",  # 数据库用户名
                    passwd="wjfuiop",  # 数据库密码
                    database="yourbay_test"
                )
        self.mycursor = self.mydb.cursor()

    def Add(self,can1,can3,can4):
        if can4 - can3 > 1001:
            print("超过1000条")
            print(can4 - can3)
        else:
            # print("输出当前需要修改的大脑激活码的跳转以及机构ID")
            leng = can4 - can3
            print(leng)
            while leng >= 0:
                bian3 = can3
                leng -= 1
                can3 += 1
                self.mycursor.execute(
                    "SELECT to_url,distributor_id,qr_code from yourbay_tst.yb_tst_brain_activation_code WHERE qr_code = %d" % (bian3))
                rows1 = self.mycursor.fetchall()
                print(bian3)
                print(rows1)
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
                        self.mycursor.execute(
                            "UPDATE yourbay_tst.yb_tst_brain_activation_code  SET to_url = 'https://h5.yourbay.net/cmsh5/#/assessDirectorHome?jgid=%d',distributor_id=%d,status =2 WHERE type=2 AND qr_code =%d" % (can1, can1, bian3))
                        self.mydb.commit()
                        file = open('增加成功.txt', 'a', encoding='UTF-8')
                        file.write("\r\n")
                        file.write(str(bian3))
                        file.close()
                        print("空的，执行成功")
            else:
                print("结束,更新完毕")



if __name__ == '__main__':
    m = MysqlUtils()

    m.Add(100007000, 100006997, 100006997)
    # MysqlUtils.Add(100007000, 10000702, 10000702)


