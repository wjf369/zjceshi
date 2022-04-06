import xlrd

class gongjulei:
    def chaxun(self):

        date= xlrd.open_workbook("C:\\Users\\sam\\Desktop\\3.xls")
        table = date.sheet_by_index(0)
        nrows = table.nrows  #获取该sheet中的有效行数
        i =0
        while i <nrows:
            hangshuju1= table.row_values(i)
            for x in hangshuju1:
                print(x)
            i += 1


# gongjulei().chaxun()
