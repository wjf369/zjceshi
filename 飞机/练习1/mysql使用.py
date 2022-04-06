import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="123456",  # 数据库密码
    database="test1"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
# mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# mycursor.executeecute("drop table sites")
# sql = 'SELECT* FROM tp_lib_book_storage WHERE owner_lib_id = 4819 AND category_id >0'
# mycursor.execute("SELECT* FROM tp_lib_book_storage WHERE owner_lib_id = 4819 AND category_id >0")
#mycursor.execute("insert into yb_book_category(book_id,isbn,title,author,author_a,publishhous,publishdate,booksize_id,country_id,language_id,subjecttype,type_id,brief,cover_photo,album,price,price_unit,pages,volume_tota,volume_id,sets_id,sets_locali,add_time,memo,class_id,age,keywords,update_time,update_uid,update_nick,title_PinYi,tst_flag,data_src_fl,book_src_id,catalogue,authorinfo,country,updatetime,bookbrand_i,editor_reco,content_rec,media_revie,preface,digest,sub_title,tst_keyword,isbn_flag,bookprize,guid,hq_flag,verify_flag,fun_questio,reading_gui,brand,cover_photo1,tst_scope,super_audit,clock_in_nu,lend_count,one_word,top_recomme,authorinfo_,brief_text,jgid,book_id_old) select  book_id,isbn,title,author,author_a,publishhous,publishdate,booksize_id,country_id,language_id,subjecttype,type_id,brief,cover_photo,album,price,price_unit,pages,volume_tota,volume_id,sets_id,sets_locali,add_time,memo,class_id,age,keywords,update_time,update_uid,update_nick,title_PinYi,tst_flag,data_src_fl,book_src_id,catalogue,authorinfo,country,updatetime,bookbrand_i,editor_reco,content_rec,media_revie,preface,digest,sub_title,tst_keyword,isbn_flag,bookprize,guid,hq_flag,verify_flag,fun_questio,reading_gui,brand,cover_photo1,tst_scope,super_audit,clock_in_nu,lend_count,one_word,top_recomme,authorinfo_,brief_text, %d as jgid,book_id as book_id_old from tp_lib_book_category WHERE tp_lib_book_category.book_id=%d"  % (2, 50450))
# for f in mycursor.fetchall():
#     print ("ip is %s, dns is %s" % (f[0], f[1]))
# for i in range(1,10):
#     mycursor.execute("insert into user(name ,age) values('%s','%d')" %('name'+str(i), int(i)))
# mydb.commit()

# sql2 = "select * from user"
#
sql1 = "SELECT tp_lib_book_category.book_id from tp_lib_book_category,tp_lib_book_storage WHERE 	tp_lib_book_storage.category_id = tp_lib_book_category.book_id"
# sql3 ="insert into yb_book_category(book_id,isbn,title,author,author_a,publishhous,publishdate,booksize_id,country_id,language_id,subjecttype,type_id,brief,cover_photo,album,price,price_unit,pages,volume_tota,volume_id,sets_id,sets_locali,add_time,memo,class_id,age,keywords,update_time,update_uid,update_nick,title_PinYi,tst_flag,data_src_fl,book_src_id,catalogue,authorinfo,country,updatetime,bookbrand_i,editor_reco,content_rec,media_revie,preface,digest,sub_title,tst_keyword,isbn_flag,bookprize,guid,hq_flag,verify_flag,fun_questio,reading_gui,brand,cover_photo1,tst_scope,super_audit,clock_in_nu,lend_count,one_word,top_recomme,authorinfo_,brief_text,jgid,book_id_old) select  book_id,isbn,title,author,author_a,publishhous,publishdate,booksize_id,country_id,language_id,subjecttype,type_id,brief,cover_photo,album,price,price_unit,pages,volume_tota,volume_id,sets_id,sets_locali,add_time,memo,class_id,age,keywords,update_time,update_uid,update_nick,title_PinYi,tst_flag,data_src_fl,book_src_id,catalogue,authorinfo,country,updatetime,bookbrand_i,editor_reco,content_rec,media_revie,preface,digest,sub_title,tst_keyword,isbn_flag,bookprize,guid,hq_flag,verify_flag,fun_questio,reading_gui,brand,cover_photo1,tst_scope,super_audit,clock_in_nu,lend_count,one_word,top_recomme,authorinfo_,brief_text,jgid,book_id_old1 as jgid,book_id as book_id_oldfrom tp_lib_book_category WHERE tp_lib_book_category.book_id=50433"
# mycursor.execute(sql)

# num = int(mycursor.rowcount)
# print(num)
# for i in range(num):
# #每次取出一行，放到 row 中，这是一个元组(id,name)
#     row = mycursor.fetchone()
# #直接输出两个元素
#     print(i)
#     print(row[0])
# rows = mycursor.fetchall()
# print(rows)
# rows = mycursor.rowcount
# print(len(rows))
# for row in rows:
#     for i in range(len(row)):


# mycursor.execute("insert into yb_book_category(book_id,isbn,title,author,author_a,publishhous,publishdate,booksize_id,country_id,language_id,subjecttype,type_id,brief,cover_photo,album,price,price_unit,pages,volume_tota,volume_id,sets_id,sets_locali,add_time,memo,class_id,age,keywords,update_time,update_uid,update_nick,title_PinYi,tst_flag,data_src_fl,book_src_id,catalogue,authorinfo,country,updatetime,bookbrand_i,editor_reco,content_rec,media_revie,preface,digest,sub_title,tst_keyword,isbn_flag,bookprize,guid,hq_flag,verify_flag,fun_questio,reading_gui,brand,cover_photo1,tst_scope,super_audit,clock_in_nu,lend_count,one_word,top_recomme,authorinfo_,brief_text,jgid,book_id_old) select  book_id,isbn,title,author,author_a,publishhous,publishdate,booksize_id,country_id,language_id,subjecttype,type_id,brief,cover_photo,album,price,price_unit,pages,volume_tota,volume_id,sets_id,sets_locali,add_time,memo,class_id,age,keywords,update_time,update_uid,update_nick,title_PinYi,tst_flag,data_src_fl,book_src_id,catalogue,authorinfo,country,updatetime,bookbrand_i,editor_reco,content_rec,media_revie,preface,digest,sub_title,tst_keyword,isbn_flag,bookprize,guid,hq_flag,verify_flag,fun_questio,reading_gui,brand,cover_photo1,tst_scope,super_audit,clock_in_nu,lend_count,one_word,top_recomme,authorinfo_,brief_text, %d as jgid,book_id as book_id_old from tp_lib_book_category WHERE tp_lib_book_category.book_id=%d" % (2, 50450))

# mycursor.execute("insert into yb_book_category(book_id,isbn,title,author,author_a,publishhous,publishdate,booksize_id,country_id,language_id,subjecttype,type_id,brief,cover_photo,album,price,price_unit,pages,volume_tota,volume_id,sets_id,sets_locali,add_time,memo,class_id,age,keywords,update_time,update_uid,update_nick,title_PinYi,tst_flag,data_src_fl,book_src_id,catalogue,authorinfo,country,updatetime,bookbrand_i,editor_reco,content_rec,media_revie,preface,digest,sub_title,tst_keyword,isbn_flag,bookprize,guid,hq_flag,verify_flag,fun_questio,reading_gui,brand,cover_photo1,tst_scope,super_audit,clock_in_nu,lend_count,one_word,top_recomme,authorinfo_,brief_text,jgid,book_id_old) select  book_id,isbn,title,author,author_a,publishhous,publishdate,booksize_id,country_id,language_id,subjecttype,type_id,brief,cover_photo,album,price,price_unit,pages,volume_tota,volume_id,sets_id,sets_locali,add_time,memo,class_id,age,keywords,update_time,update_uid,update_nick,title_PinYi,tst_flag,data_src_fl,book_src_id,catalogue,authorinfo,country,updatetime,bookbrand_i,editor_reco,content_rec,media_revie,preface,digest,sub_title,tst_keyword,isbn_flag,bookprize,guid,hq_flag,verify_flag,fun_questio,reading_gui,brand,cover_photo1,tst_scope,super_audit,clock_in_nu,lend_count,one_word,top_recomme,authorinfo_,brief_text, %d as jgid,book_id as book_id_old from tp_lib_book_category WHERE tp_lib_book_category.book_id=%d"  % (2, 50450))
# mydb.commit()

# sql1 = "SELECT tp_lib_book_category.book_id from tp_lib_book_category,tp_lib_book_storage WHERE tp_lib_book_storage.category_id = tp_lib_book_category.book_id"
mycursor.execute("SELECT book_id_old FROM yb_book_category WHERE jgid=2")
xinbiaoyiyou = mycursor.fetchall()
print(xinbiaoyiyou)
mycursor.execute(sql1)
rows = mycursor.fetchall()
# print(rows)
q = 0
for row in rows:

    for i in range(len(row)):
        # print(row[i])

        # if row[i] in
        # mycursor.execute("insert into yb_book_category(isbn,title,author,author_a,publishhous,publishdate,booksize_id,country_id,language_id,subjecttype,type_id,brief,cover_photo,album,price,price_unit,pages,volume_tota,volume_id,sets_id,sets_locali,add_time,memo,class_id,age,keywords,update_time,update_uid,update_nick,title_PinYi,tst_flag,data_src_fl,book_src_id,catalogue,authorinfo,country,updatetime,bookbrand_i,editor_reco,content_rec,media_revie,preface,digest,sub_title,tst_keyword,isbn_flag,bookprize,guid,hq_flag,verify_flag,fun_questio,reading_gui,brand,cover_photo1,tst_scope,super_audit,clock_in_nu,lend_count,one_word,top_recomme,authorinfo_,brief_text,jgid,book_id_old) select  isbn,title,author,author_a,publishhous,publishdate,booksize_id,country_id,language_id,subjecttype,type_id,brief,cover_photo,album,price,price_unit,pages,volume_tota,volume_id,sets_id,sets_locali,add_time,memo,class_id,age,keywords,update_time,update_uid,update_nick,title_PinYi,tst_flag,data_src_fl,book_src_id,catalogue,authorinfo,country,updatetime,bookbrand_i,editor_reco,content_rec,media_revie,preface,digest,sub_title,tst_keyword,isbn_flag,bookprize,guid,hq_flag,verify_flag,fun_questio,reading_gui,brand,cover_photo1,tst_scope,super_audit,clock_in_nu,lend_count,one_word,top_recomme,authorinfo_,brief_text, %d as jgid,book_id as book_id_old from tp_lib_book_category WHERE tp_lib_book_category.book_id=%d"  % (2, row[i]))
        mydb.commit()
        q+=1
print(q)









