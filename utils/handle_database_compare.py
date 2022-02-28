# -*- coding: utf-8 -*-
# @Time: 2022/2/22 17:56
# @Author: shenyuming

import requests,re,openpyxl
import json,time,datetime

'''
    读取两个数据库数据，然后对比， 数据相同的跳过， 数据不同的写入excel
'''

def test_QueryData(o):  ##查询接口
    wb = openpyxl.Workbook()
    ws = wb.active

    url1 = "http://192.168.220.150:8713/agilorapi/v6/query?db=AGILOR_RTDB"
    url2 = "http://192.168.220.130:8713/agilorapi/v6/query?db=AGILOR_RTDB"

    headers = {
        'Authorization': 'Token XXX',
        'Content-Type': 'application/vnd.agilorql',
        'Accept': 'application/csv'
    }

    data = 'select * from T1 limit 10000 offset ' + str(o)


    response1 = requests.post(url1, headers=headers, data=data)
    response2 = requests.post(url2,headers=headers,data=data)

    ## 正则处理数据，以\n\t分割数据，返回list
    lista = re.split(r'[\n\t]', response1.text)
    listb = re.split(r'[\n\t]', response2.text)
    print('lista----------',lista)
    print('listb----------', listb)

    if lista == listb:
        print('备份前与备份后一致')
    else:
        print('第' + str(o/10000 + 1) + '个10000条不一致')
        listresulta = []
        for i in range(1, len(lista) - 1):  # 把普通列表转成嵌套列表
            li = []
            li.append(lista[i])
            listresulta.append(li)

        listresultb = []
        for i in range(1, len(listb) - 1):  # 把普通列表转成嵌套列表
            li2 = []
            li2.append(listb[i])
            listresultb.append(li2)
        # print(listresulta)

        for r in range(len(listresulta)):
            listc = listresulta[r][0].split(',')
            for c in range(len(listc)):
                ws.cell(r + 1, c + 1).value = listc[c]
        wb.save('E:\sym\全量数据\全量lista0222\第' + str(o/10000 + 1) + '个10000条a.xlsx')

        for r in range(len(listresultb)):
            listc = listresultb[r][0].split(',')
            for c in range(len(listc)):
                ws.cell(r + 1, c + 1).value = listc[c]
        wb.save('E:\sym\全量数据\全量listb0222\第' + str(o/10000 + 1) + '个10000条b.xlsx')


if __name__ == '__main__':
    count = 50000
    times = count//10000

    for i in range(0,times):  # 一次查询的数据量存成1个excel，遍历查询
        offset = 10000 * i
        test_QueryData(offset)