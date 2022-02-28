# -*- coding: utf-8 -*-
# @Time: 2022/2/24 11:52
# @Author: shenyuming

from openpyxl import Workbook
from openpyxl.utils import get_column_letter

'''
    写入新的工作簿
'''
wb = Workbook()

dest_filename = '../excelData/empty_book.xlsx'
ws1 = wb.active
ws1.title = 'range names'
for row in range(1,40):     # 行，30行
    ws1.append(range(600))  # 列，599列， 每列写入对应列的数字

ws2 = wb.create_sheet(title='PI')   # 创建新的工作表，
ws2['F5'] = 3.14                    # 单元格赋值

ws3 = wb.create_sheet(title='Data')     #创建第三个工作表
for row in range(10,20):                #行，第10行到第19行
    for col in range(27,54):            #列，第27列到第53列
        _ = ws3.cell(column=col,row=row,value="{0}".format(get_column_letter(col)))   # 写入对应列的字母
print('ws3的数据：',ws3['AA10'].value)   # 打印单元格值
for row in ws3.values:          # 循环打印excel的所有单元格值
    for col in row:
        # print('循环打印excel的所有值',col)
        pass
wb.save(filename=dest_filename)

'''
    打开现有工作簿
'''
from openpyxl import load_workbook
wb = load_workbook(filename='../excelData/empty_book.xlsx')
sheet_ranges = wb['range names']
print(sheet_ranges['D36'].value)


'''
    新工作簿写入
    使用数字格式
'''
import datetime
wb = Workbook()
ws = wb.active
ws['A1'] = datetime.datetime(2020,7,20)
print(ws['A1'].number_format)

'''
    使用公式
'''
ws['B1'] = "=SUM(1,1)"
wb.save('../excelData/formula.xlsx')

