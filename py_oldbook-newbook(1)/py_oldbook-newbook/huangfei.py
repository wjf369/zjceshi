#!usr/bin/python
# -*- coding: utf-8 -*-
import pymysql

#图书插入
def book_info(excel):
    conn = pymysql.connect(host='39.98.169.249',port=3306,user='dev_wujinfa',passwd='wjfuiop',db='yourbay_test',charset='utf8')#测试库地址
    cursor = conn.cursor()
    cursor.execute('SELECT res_id,contact_name,title,fudd FROM tp_nbv_res_jgmp WHERE title like "河北唐山友谊天地悠贝馆"  and flag=1 and  ownerby IN (SELECT uid FROM tp_nbv_userinfo WHERE mobile= %s)' , (excel))
    return cursor.fetchall()
print(book_info('18701635531'))
