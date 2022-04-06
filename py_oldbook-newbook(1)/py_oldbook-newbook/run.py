#!usr/bin/python
# -*- coding: utf-8 -*-
import pymysql
import time,datetime
import pandas  as pd
import json,gongju
import sqls
with open("log.txt","w",encoding='utf-8') as txt:
    try:
        #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
        # conn = pymysql.connect(host='rm-8vb6yntx7c0i3b51kbo.mysql.zhangbei.rds.aliyuncs.com',port=3306,user='dev_wujinfa',passwd='wjfuiop',db='yourbay',charset='utf8')#正式库地址
        conn = pymysql.connect(host='39.98.169.249',port=3306,user='dev_wujinfa',passwd='wjfuiop',db='yourbay_test',charset='utf8')#测试库地址
        # conn = pymysql.connect(host='rm-8vb6yntx7c0i3b51kbo.mysql.zhangbei.rds.aliyuncs.com',port=3306,user='dev_wujinfa',passwd='wjfuiop',db='yourbay',charset='utf8')#Linux连接正式库库地址
        # conn = pymysql.connect(host='rm-8vbn6p036x0t6s8qjco.mysql.zhangbei.rds.aliyuncs.com',port=3306,user='dev_wujinfa',passwd='wjfuiop',db='yourbay',charset='utf8')#数据备份库
        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        cursor.execute(sqls.select_jgmp_id())

        # 获取所有场馆ID记录列表
        results = list(cursor.fetchall())
        #执行获取yb_book_category表列名
        cursor.execute(sqls.category_COLUMN_NAME())
        COLUMN_NAME = cursor.fetchall()
        book_category_list = []
        for COLUMN_NAME_ in COLUMN_NAME:
            COLUMN_NAME_field = COLUMN_NAME_[0]
            if COLUMN_NAME_field != "book_id":
                book_category_list.append(COLUMN_NAME_field)

        book_category_str_3 = ""
        #将列名拼装成sql使用内容（拼装新表字段sql）
        for book_category_str_1 in book_category_list:
            book_category_str_2 = str(book_category_str_1)
            book_category_str_3 = book_category_str_3 + book_category_str_2
            book_category_str_3= book_category_str_3 + ","
        book_category_str = book_category_str_3[:-1] + " "


        for res_id in results:#截取场馆ID
            jgmp_id = res_id[0]#处理ID，方便识别
            cursor.execute(sqls.select_book_storage_owner_lib_id(),(jgmp_id))
            category_id = list(cursor.fetchall())
            

            if category_id != []:
                for i in category_id: #截取老图书ID
                    book_id_old = i[0]#处理ID，方便识别
                    if book_id_old != None:
                        # cursor.execute(sqls.select_book_category(),(book_category_str,book_id_old))
                        select_book_category_  = sqls.select_book_category(book_category_str)
                        cursor.execute(select_book_category_,(book_id_old))
                        book_category = cursor.fetchall()

                        if list(book_category) != []:
                            book_category = list(book_category[0])
                            book_category_value_lsit = []

                            # for j in book_category:
                                # if j == None:
                                #     book_category_value_lsit.append('')
                                # else:
                                # book_category_value_lsit.append(str(j))
                            try:
                                for l in range(len(book_category_list)):
                                    if book_category_list[l] == 'add_time' and book_category[l] != None:
                                        book_category[l] = book_category[l].isoformat()
                                    if book_category_list[l] == 'update_time' and book_category[l] != None:
                                        book_category[l] = book_category[l].isoformat()
                                    if book_category_list[l] == 'updatetime' and book_category[l] != None:
                                        book_category[l] = book_category[l].isoformat()
                                    # if book_category_list[l] == 'publishdate' and book_category[l] != None and book_category[l] != '0000-00-00':
                                    #     book_category[l] = book_category[l].isoformat()
                                    if book_category_list[l] == "publishdate" and book_category[l] == None:
                                        book_category[l] = '0000-00-00'       
                            except AttributeError:
                                print("鬼知道发生啥了,详细数据：\n",book_category,file=txt)        
                                print("鬼知道发生啥了,详细数据：\n",book_category)
                                break 



                            book_category_str_new = str(book_category_str) +  ",book_id_old" + ",jgid"  #拼接新库新增字段
                            book_category_list_new = book_category_str_new
                            book_category.append(str(book_id_old))
                            book_category.append(str(jgmp_id))
                            book_category_value_str_ = str(tuple(book_category))
                            book_category_value_str = book_category_value_str_.replace(' ','')
                            book_category_value_str= book_category_value_str_.replace('None','null')


                            book_category_list_new = book_category_list_new.split(",")
                            for v in range(len(book_category_list_new)):
                                if book_category_list_new[v] == 'title':
                                    title_number = v
                                if book_category_list_new[v] == 'isbn':
                                    isbn_number = v
                                if book_category_list_new[v] == 'jgid':
                                    jgid_number = v
                            cursor.execute(sqls.yb_book_category_lianhe(),(book_category[title_number],book_category[isbn_number],book_category[jgid_number]))
                        
                            if list(cursor.fetchall()) != []:
                                break

                            book_category_value_ycl = gongju.YCL(book_category_value_str)
                            insert_book_category = sqls.insert_book_category_new(book_category_str_new,book_category_value_str)
                            cursor.execute(insert_book_category)
                            conn.commit()
                            print("已插入：",book_id_old)
                
                        else:
                            print("ERROR！场馆ID：",res_id[0],",所关联书籍ID：",book_id_old,"，在老库中不存在\n",file=txt)
                            print("ERROR！场馆ID：",res_id[0],",所关联书籍ID：",book_id_old,"，在老库中不存在")
                else:
                    print("机构：",jgmp_id,"在馆藏中所关联图书没有【category_ID】\n",file=txt)
                    print("机构：",jgmp_id,"在馆藏中所关联图书没有【category_ID】")
            else:
                print("机构：",jgmp_id,"，没有关联图书\n",file=txt)
                print("机构：",jgmp_id,"，没有关联图书")


        # 获取所有记录列表
        # results = cursor.fetchall()
    # except Exception as e:
    #         #错误回滚
    #     print("出现问题",book_id)
        # conn.rollback()
    finally:
        conn.close()
txt.close()