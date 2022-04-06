#!usr/bin/python
# -*- coding: utf-8 -*-
#新表的category字段名获取
def category_COLUMN_NAME():
   category_COLUMN_NAME = "select COLUMN_NAME from information_schema.COLUMNS where table_name = 'tp_lib_book_category'and TABLE_SCHEMA = 'yourbay_test';"
   return category_COLUMN_NAME
#机构表-机构（场馆）ID
def select_jgmp_id():
    select_jgmp_id = "select res_id from yourbay_test.tp_nbv_res_jgmp;"
    return select_jgmp_id
#馆藏表-场馆ID
def select_book_storage_owner_lib_id():
    category_id ="select category_id from yourbay_test.tp_lib_book_storage where owner_lib_id = %s and category_id > 0;"
    return category_id
def select_book_category(book_category_List_name):#book_category_list_
    #book_category_old = "select isbn, title, author, author_a, publishhouse_id, publishdate, booksize_id, country_id, language_id, subjecttype_id, type_id, brief, cover_photo, album, price, price_unit, pages, volume_total, volume_id, sets_id, sets_localid, add_time, memo, class_id, age, keywords, update_time, update_uid, update_nickname, title_PinYin, tst_flag, data_src_flag, book_src_id, catalogue, authorinfo, country, updatetime, bookbrand_id, editor_recommend, content_recommend, media_reviews, preface, digest, sub_title, tst_keywords, isbn_flag, bookprize, guid, hq_flag, verify_flag, fun_question, reading_guide, brand, cover_photo_custom, tst_scope, super_audit_flag, clock_in_num, lend_count, one_word, top_recommend, authorinfo_text, brief_text from yourbay_test.tp_lib_book_category where book_id = %s;"
    book_category_old_1 = 'select '
    book_category_old_2 = book_category_List_name
    book_category_old_3 = ' from yourbay_test.tp_lib_book_category where book_id = %s;'
    return book_category_old_1+book_category_old_2+book_category_old_3
#insert sql语句拼接
def insert_book_category_new(book_category_List_name,book_category_value): 
    insert_book_category_new_1 = 'INSERT INTO yourbay_test.yb_book_category ('
    insert_book_category_new_2 = book_category_List_name
    insert_book_category_new_3 = ') VALUES '
    insert_book_category_new_4 = book_category_value + ';'
    insert_book_category_new_5 = insert_book_category_new_1+insert_book_category_new_2+insert_book_category_new_3+insert_book_category_new_4
    return insert_book_category_new_5

def yb_book_category_lianhe():
    yb_book_category_lianhe_ = 'select title,isbn,jgid from yourbay_test.yb_book_category where title = %s and isbn = %s and jgid = %s'
    return yb_book_category_lianhe_