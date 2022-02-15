# -*- coding: utf-8 -*-
# @Time: 2022/1/21 14:22
# @Author: shenyuming

import requests,re,openpyxl
import json

# def test_Query(num):
#
#     url = "http://106.39.185.104:8713/agilorapi/v6/query?db=AGILOR_RTDB"
#
#     payload = "select * from T1 limit 10000 offset" + str(num)
#     headers = {
#         'Accept': 'application/csv',
#         'Content-Type': 'application/vnd.agilorql',
#         'Authorization': 'Token NcBoqGPHg92sihD-fiFxaLfsrw0H8pC0q8OJvaWmOtvWuYFrAZTb2pgEX3kcVxLfZ1SxON9kPqRHHiLRrv-Bsw=='
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#     ## 表头替换为空
#     res = response.text.replace('name,tags,time,AGPOINTNAME,B,F,L,S','')
#     lista = re.split(r'\n',res)
#     listall = []
#     for i in range(1,len(lista)-1):
#         li1 = []
#         li1.append(lista[i])
#         listall.append(li1)
#
#     print('listall添加的结果---->', listall)
#     return listall
#
#
# def data_Write(path,new_list):
#     tq = test_Query()
#

"""
    中国系统 -- 1亿数据分批次导出大量数据到excel,每次一百万

"""

def test_QueryData(l, o):  ##查询接口
    url = "http://106.39.185.104:8713/agilorapi/v6/query?db=AGILOR_RTDB"
    data = 'select * from T1 limit ' + str(l) + ' offset ' + str(o)

    headers = {
        'Authorization': 'Token NcBoqGPHg92sihD-fiFxaLfsrw0H8pC0q8OJvaWmOtvWuYFrAZTb2pgEX3kcVxLfZ1SxON9kPqRHHiLRrv-Bsw==',
        'Content-Type': 'application/vnd.agilorql',
        'Accept': 'application/csv'
    }
    response = requests.post(url, headers=headers, data=data)

    ## 正则处理数据，以\n\t分割数据，返回list
    lista = re.split(r'[\n\t]', response.text)

    ## 存放全部数据
    listresult = []

    for i in range(1, len(lista) - 1):  # 把普通列表转成嵌套列表
        li = []
        li.append(lista[i])
        listresult.append(li)

    return listresult


def writeToExcel(file_path, new_list):
    wb = openpyxl.Workbook()
    ws = wb.active
    # ws.title = '明细'
    for r in range(len(new_list)):
        for c in range(len(new_list[0])):
            ws.cell(r + 1, c + 1).value = new_list[r][c]
            # excel中的行和列是从1开始计数的，所以需要+1
    wb.save(file_path)  # 注意，写入后一定要保存
    return 1

if __name__ == '__main__':
    limit = 1000000  # 一次所查询的数据量，受excel存储限制，最大100w条
    count = 100
    for i in range(99, 101):  # 一次查询的数据量存成1个excel，遍历查询
        offset = limit * i
        total_list = test_QueryData(limit, offset)
        writeToExcel('E:\sym\全量数据\全量1\第' + str(i + 1) + '个' + str(limit) + '条.xlsx', total_list)
        print('这是第%d个excel完成' %count)
        count+=1
'''
name,       tags,       time,               AGPOINTNAME,        B,          F,                  L,          S
T1,             ,       1642734682916293946,    tag_F_1,         ,          45226.4006899,       ,
T1,             ,       1642734682916293946,    tag_F_10,        ,          79937.8420698,       ,

T1,             ,       1642734683624432481,    tag_L_1,         ,          ,                 44251,
T1,             ,       1642734683624432481,    tag_L_100,       ,          ,                 58713,

T1,             ,       1642734683985583212,    tag_S_1213,       ,         ,                      ,          6e71bbaa-101e-4e11-9d89-5066ccd5ce37
T1,             ,       1642734683985583212,    tag_S_1218,       ,         ,                      ,          3edf901e-2335-46b0-9d1b-e2f5071dd70a

T1,             ,       1642734684305415746,    tag_B_1483,     true,       ,                       ,
T1,             ,       1642734684305415746,    tag_B_1486,     true,       ,                       ,
'''