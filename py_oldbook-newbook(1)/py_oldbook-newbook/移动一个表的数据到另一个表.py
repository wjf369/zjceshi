import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="123456",  # 数据库密码
    database="test1"
)



mycursor = mydb.cursor()


# print(mycursor)
mycursor.execute("SELECT * FROM user2  WHERE age=5")

rows = mycursor.fetchall()
# print(rows) #[(28, 'name6', 6), (37, 'name6', 6)]
for row in rows:
    mycursor.execute("SELECT * from newuser WHERE old_id in (SELECT id FROM user2 where id = %d)" %(row[0]))
    lens = mycursor.fetchall()
    print(lens)
    if lens :
        print("已经存在这条数据")
        print(row)
    else:
        mycursor.execute("INSERT INTO newuser (name,age,old_id) VALUES('%s','%d','%d')" % (row[1], row[2], row[0]))
        print("zhixing")
        mydb.commit()
