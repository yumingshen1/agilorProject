# -*- coding: utf-8 -*-
# @Time: 2022/2/16 16:38
# @Author: shenyuming

'''
    判断第一个excel中是否包含第二个excel的数据
'''

import xlrd
import xlwt
import xlutils
from xlutils.copy import copy

# 打开表格并获取
allTable = xlrd.open_workbook("E:/sym/pi解析/pi2d1m_interpolated/CDEP158.xlsx")
allShell = allTable.sheet_by_index(0)
allCol = allShell.col_values(1)

myTable = xlrd.open_workbook("E:/sym/pi解析/pi_interpolated/CDEP158.xlsx")
myShell = myTable.sheet_by_index(0)
myCol = myShell.col_values(1)


hasList = []
# myShell 一共有26行,
for i in range(26):
    # 判断分表指定数据是否在总表存在
    if myCol[i] in allCol:
        # 如果存在存储索引并执行下一个循环
        hasList.append(i)
        continue

print(hasList)

# 保存数据到新表
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('Worksheet')

# 循环遍历出匹配到的数据的索引值
for n in hasList:
    # 获取到整行数据
    myRow = myShell.row_values(n)
    # 数据有31列
    for i in range(4):
        # 参数（行，列，插入值）
        worksheet.write(n,i,myRow[i])

# 保存
workbook.save('E:/sym/pi解析/匹配5.xlsx')

