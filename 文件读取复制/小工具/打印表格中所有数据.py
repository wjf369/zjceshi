import  xlrd

date= xlrd.open_workbook("C:\\Users\\sam\\Desktop\\3.xls")
# date= xlrd.open_workbook("C:\\Users\\sam\\Desktop\\3 - 副本.xls")

table = date.sheet_by_index(0)
# hangshuju = table.row_values(0, start_colx=0, end_colx=None)   #返回由该行中所有单元格的数据组成的列表 [55196.0, '9787552621518', '雨蛙老师的趣味自然课',
# print(hangshuju)

ncols = table.ncols#获取列表的有效列数
nrows = table.nrows  #获取该sheet中的有效行数

#____________________________迭代器
# print(nrows)
# i = 0
# while i < nrows:
#     hangshuju = table.row_values(i, start_colx=0, end_colx=None)
#
#     it = iter(hangshuju)
#     for x in it :
#         print(x)
#     i += 1


#____________________________for 循环


i =0
while i <nrows:
    hangshuju1= table.row_values(i)
    l = len(hangshuju1)
    leixing= table.row_slice(i)
    # print(leixing)
    for x in hangshuju1:
        # print(x)
        if x:
            pass
        else:
            print("有空值",i)
    i+=1


