# -*- coding: utf-8 -*-
# @Time: 2022/2/18 15:52
# @Author: shenyuming

import   xlrd
def read_excel(fileName):
    global newset
    newset = set()
    global  listdata
    listdata = []
    bk=xlrd.open_workbook(fileName)
    # shxrange=range(bk.nsheets)
    # print(bk.sheet_names())
    #获取指定sheet名字
    sheetName = bk.sheet_by_name('Sheet1')
    # print(sheetName.name)
    #获取总行数：
    rowNum = sheetName.nrows
    # print(rowNum)
    #获取总列数
    colNum = sheetName.ncols
    #获取文件中内容
    for  i  in  range(0,rowNum):
        global  rowdata
        rowdata =''
        for j  in range(0,colNum):

            # print(sheetName.cell_value(i,j),end='  ')
            data = sheetName.cell_value(i,j)
            # print(data)
            rowdata += data+' '
        # print('\n')
        # print(rowdata)
        newset.add(rowdata)
    # print(newset)
    return newset
set1 = read_excel(f'E:/sym/pi解析/pi_Interpolated_1s/DL-SW001-MMJCYX-1SJ-S-PLANTCONNECT.xlsx')
set2 = read_excel(f'E:/sym/pi解析/PI1d1s_interpolated_1s/DL-SW001-MMJCYX-1SJ-S-PLANTCONNECT.xlsx')

print('list1list2 相同：%s'%len(set1.intersection(set2)))
print('不同：%s'%len(set2.difference(set1)))