# -*- coding: utf-8 -*-
import xdrlib ,sys
import xlrd
import time
def open_execel(file = '/home/jdliu/test/test.xls'):
	try:
	    data = xlrd.open_workbook(file)
	    return data
	except Exception as e:
	    print(str(e))


def execel_table_byindex(file = '/home/jdliu/test/test.xls', colnameindex=0, by_index=0, date_index=6, time_index=7):
	data = open_execel(file)
	table = data.sheets()[by_index]	
	nrows = table.nrows
	early = {}
	late = {}
	tmp_date = ""
	print(nrows)
	for rownum in range(1,nrows):

	    row = table.row_values(rownum)

	    if row:		
                if tmp_date != row[date_index] :
                    early[row[date_index]] = row[time_index]
                    late[row[date_index]] = row[time_index]
                    tmp_date = row[date_index]
		
                else:
                    late[row[date_index]] = row[time_index]

	for e, l in early.items():
	    if (str(late[e]) > "20:00"):
                print(e + ":" + str(l) + "," + str(late[e]) + "\n")

if __name__ == "__main__":
    execel_table_byindex()
