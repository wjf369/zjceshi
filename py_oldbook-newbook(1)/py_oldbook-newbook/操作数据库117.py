import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="123456",  # 数据库密码
    database="test1"
)

mycursor = mydb.cursor()

# print(mycursor)

def chuancan(canshu):

    mycursor.execute("SELECT age FROM user2  WHERE id=%s" % (canshu))
    rows = mycursor.fetchall()
    print(rows)
    for row in rows:
        mycursor.execute("UPDATE user2 SET name='5sui' where age =%s" % (row[0]))
        mydb.commit()


chuancan(36)
