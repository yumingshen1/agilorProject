# -*- coding: utf-8 -*-
# @Time: 2021/12/6 10:50
# @Author: shenyuming

import xlrd
'''
    读取excel
'''
#打开一个excel
workbook = xlrd.open_workbook(f'E:/sym/pi解析/pi web api(2).xlsx')

## 定位到某个sheet页面
worksheet1 = workbook.sheet_by_name(u'Sheet1')
print('精准sheet页面，%s' %worksheet1)

## 遍历sheet页面的所有行
num_row = worksheet1.nrows
print('sheet的总行数，%s'%num_row)
for curr_row in range(num_row):
    row = worksheet1.row_values(curr_row)
    # print('row%s is %s' %(curr_row,row)+'\n')

## 遍历sheet的所有的列
num_col = worksheet1.ncols
print('sheet的总列数，%s' %num_col)
for curr_col in range(num_col):
    col = worksheet1.col_values(curr_col)
    # print('col%s is %s' %(curr_col,col)+'\n')

## 遍历所有的单元格数据
for rown in range(num_row):
    for coln in range(num_col):
        num_cell = worksheet1.cell_value(rown,coln)
        # print('搜有的数据---%s'%num_cell)

        ## 或者这种写法
        cell = worksheet1.cell(rown, coln).value
        # print('全部的cell数据 %s' % cell)

        ###  获取cell值得类型  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
        cell_type = worksheet1.cell_type(rown,coln)
        # print('类型---》 %s' %cell_type)

## 索引定位
worksheet2 = workbook.sheet_by_index(0)
print('索引定位sheet页面 %s' %worksheet2)
workbook2 = workbook.sheets()[0]
print('索引定位sheet页面 %s' %worksheet2)

# 抓取所有的sheet页面
worksheets = workbook.sheet_names()
print('worksheets is %s' %worksheets)

## 遍历所有的sheet页面
for workheet_name in worksheets:
    worksheet = workbook.sheet_by_name(workheet_name)
    print('所有的sheet页面，%s'%worksheet)

'''
    写入excel
'''
import xlwt
wbk = xlwt.Workbook()           ## 创建excel
sheet = wbk.add_sheet('Sheet1') ## 创建sheet页面
sheet.write(0,1,'testcase')   ## cell(0,1) 写入数据
wbk.save('./testcase.xlsx')


'''
    修改excel文件  xlrd + xlutils
'''
from xlutils.copy import copy
workbook = xlrd.open_workbook('./testCase.xlsx')    #打开一个文件
workbooknew = copy(workbook)    ## 复制下原有的excel
ws = workbooknew.get_sheet(0)   ## 获得第一个sheet页面
ws.write(0,2,'change')
workbooknew.save('./testCasenew.xlsx')


'''
    excel读写操作 openpyxl
'''
import os,openpyxl
filename = 'E:/sym/4.2迁移/1.xlsx'
wb = openpyxl.load_workbook(filename) #打开已有的excel
print(wb.sheetnames)    ##得到所有的sheetname
## 遍历工作簿的sheet
for sheet in wb:
    print(sheet)
## 创建sheet
mySheet = wb.create_sheet('Sheet2')
print(mySheet)

##操作某一个sheet页
sheet2 = wb.get_sheet_by_name('Sheet2')
sheet2 = wb['Sheet2']

## 取活跃的sheet,默认第一个
ws = wb.active
print(ws)
print(ws['A1'])
print(ws['A1'].value)

## 拿取单元格数据
c = ws['B1']
print('row {},col {} is {}'.format(c.row,c.colunm,c.value))
print('cell {} is {}\n'.format(c.coordinate,c.value))

print(ws.cell(row=1,column=2).value)

for i in range(1,8,2):  ##遍历第二列数据
    print(i,ws.cell(row=i,column=2).value)

# def openpytest(new_file):
#     if os.path.exists(new_file):
#         new_web = load_workbook(new_file)
#         sheet_names = new_web.get_sheet_names()  ##得到工作簿所有的表
#         ws = new_web.get_sheet_by_name(sheet_names[0])
#         print('ws的值--%s,' % ws)
#     else:
#         wb = Workbook()     ##创建一个工作簿
#         wb = load_workbook('./testcase.xlsx')     ##打开已有的workbook
#         sheet_names = wb.get_sheet_names()    ##得到工作簿所有的表
#         ws = wb.get_sheet_by_name(sheet_names[0])
#         print('ws的值--%s,' %ws)
#
#


if __name__ == '__main__':
    # openpytest('./testcase.xlsx')
    pass


'''
4.2-->6.0:
,result,table,_start,_stop,_time,_value,AGPOINTNAME,_field,_table
,_result,0,2021-11-23T03:07:00.408151759Z,2021-11-26T02:07:00.408151759Z,2021-11-23T03:07:01Z,true,Simu1_1,B,test_table

,_result,1,2021-11-23T03:07:00.408151759Z,2021-11-26T02:07:00.408151759Z,2021-11-23T03:07:01Z,8208,Simu1_1,state,test_table

PI:
,result,table,_start,_stop,_time,_value,AGPOINTNAME,_field,_table
,_result,0,2021-12-07T05:00:00.000000001Z,2021-12-13T21:27:51.030181106Z,2021-12-07T05:00:25Z,50,sy.st.WIN-F9KROVHMQ74.random1.sc1,F,PI_TABLE

,_result,1,2021-12-07T05:00:00.000000001Z,2021-12-13T21:27:51.030181106Z,2021-12-07T05:00:25Z,true,sy.st.WIN-F9KROVHMQ74.random1.sc1,Good,PI_TABLE

'''
[['sy.st.WIN-F9KROVHMQ74.random1.sc1', '2021-12-14 09:45:55', '50', 'true', 'F'], ['sy.st.WIN-F9KROVHMQ74.random1.sc1', '2021-12-14 09:46:25', '50', 'true', 'F']]
