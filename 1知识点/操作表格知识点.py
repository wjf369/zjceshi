import  xlrd

date= xlrd.open_workbook("C:\\Users\\sam\\Desktop\\3.xls")
table =date.sheet_by_index(0)
# print(table)
# hang = table.row(0)

# ————————————————————————————————————————————对行的操作————————————————————————
# nrows = table.nrows  #获取该sheet中的有效行数 4
# print(nrows)
# liebiao = table.row_slice(0)  #返回由该列中所有的单元格对象组成的列表 [number:1.0, number:2.0, number:3.0, number:4.0, number:5.0, number:6.0, number:7.0, number:8.0, number:9.0, number:10.0, number:11.0]
# print(liebiao)
# hangshujuleixing = table.row_types(0, start_colx=0, end_colx=None)    #返回由该行中所有单元格的数据类型组成的列表 array('B', [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
# print(hangshujuleixing)
# hangshuju = table.row_values(0, start_colx=0, end_colx=None)   #返回由该行中所有单元格的数据组成的列表 [55196.0, '9787552621518', '雨蛙老师的趣味自然课',
# print(hangshuju)
# len1 = table.row_len(0)#返回该列的有效单元格长度
# print(len1)

# ————————————————————————————————————————————对列的操作————————————————————————
# ncols = table.ncols#获取列表的有效列数
# table.col(0, start_rowx=0, end_rowx=None)#返回由该列中所有的单元格对象组成的列表
# table.col_slice(0, start_rowx=0, end_rowx=None)#返回由该列中所有的单元格对象组成的列表
# table.col_types(0, start_rowx=0, end_rowx=None)#返回由该列中所有单元格的数据类型组成的列表
# table.col_values(0, start_rowx=0, end_rowx=None)#返回由该列中所有单元格的数据组成的列表



# ————————————————————————————————————————————单元格的操作————————————————————————
# table.cell(rowx,colx)   #返回单元格对象  number:11.0
# print(table.cell(1,1))
# table.cell_type(rowx,colx)    #返回单元格中的数据类型 2
# print(table.cell_type(1,1))
# table.cell_value(rowx,colx)   #返回单元格中的数据 11.0
# print(table.cell_value(1,1))

# ————————————————————————————————————————————打印所有数据————————————————————————

nrows = table.nrows
ncols = table.ncols
# for i in range(nrows):
#     print(table.row_values(i))
# for i in range(ncols):
#     print(table.col_values(i))

# —————————————————————————————————————————迭代器
# print(nrows)
# i = 0
# while i < nrows:
#     hangshuju = table.row_values(i, start_colx=0, end_colx=None)
#     it = iter(hangshuju)
#     for x in it :
#         print(x)
#     i += 1


# —————————————————————————————————————————for循环
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