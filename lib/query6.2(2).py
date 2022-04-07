# coding=utf-8
import array
import datetime
import string
import time
import xlwt,xlsxwriter
import numpy as np
import requests
import json

'''
    rtdb 6.2.0 读取数据。
'''

def test_QueryData():  ##查询接口
    import requests

    url = "http://192.168.10.65:8713/agilorapi/v6/query?db=PIF1y"

    payload = "select * from PI where AGPOINTNAME = 'DL-SW001-MMJCYX-1SJ-S-PLANTCONNECT' and time <= '2022-02-06T08:25:56.000Z' and time >= '2022-01-20T01:57:43.000Z'"
    headers = {
        'Accept': 'application/csv',
        'Content-Type': 'application/vnd.agilorql',
        'Authorization': 'Token XXX'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(type(response.text))
    print('结果---》',response.text)

    re = response.text.split('\n',1)[1]
    print('截取的\n',re)

    re = re.replace('\n', '')
    lista = []
    lista.append(re)
    print('lista添加的结果---->',lista)
    return re

def countlist():  ##获取查询接口的数据，并处理数据
    tq = test_QueryData()
    tq = resolver(tq)
    listb = []
    timeMap = {}

    # 对数据根据时间进行分组
    for l in tq:
        arr = l.split(",")
        lastTime = arr[0]
        # print (lastTime)
        if timeMap.get(lastTime):
            grouped = timeMap.get(lastTime)
            grouped.append(arr)
            timeMap[lastTime] = grouped
        else:
            timeMap[lastTime] = [arr]

    # 根据 table 字段进行 冒泡排序
    for index, v in timeMap.items():
        count = len(v)
        for i in range(0, count):
            for j in range(i + 1, count):
                if v[i][0] > v[j][0]:
                    v[i], v[j] = v[j], v[i]

    for index, v in timeMap.items():
        AGPOINTNAME = v[0][1]
        date = v[0][0]
        date = date[:10]
        time_tuple_1 = time.localtime(int(date))
        bj_time = time.strftime("%Y-%m-%d %H:%M:%S", time_tuple_1)

        '''
            根据不同的点值的类型，更改value的取值 [0][2] [0][4]
        '''
        value = v[0][4]
        # print('value的值',value)
        good = v[0][3]

        row = [AGPOINTNAME,bj_time,value,good]
        listb.append(row)
        # print('listb数据',listb)
    return listb

# 解析数据转为数组 ，去除PI
def resolver(data):
    dataArr = data.split("PI,,")
    dataArr.pop(0)
    print('处理',dataArr)
    return dataArr

## 数据写入excel
def write_excel_data(filepath,data):
    filename = f'{filepath}'   # 存放excel的路径
    workbook = xlsxwriter.Workbook('{}'.format(filename))  # 建立文件
    worksheet = workbook.add_worksheet()  # 建立sheet

    format4 = workbook.add_format(
        {'font_size': '12', 'align': 'center', 'valign': 'vcenter', 'bold': True, 'font_color': '#217346',
         'bg_color': '#FFD1A4'})
    col = ['A1', 'B1', 'C1', 'D1', 'E1']
    title = [u'AGPOINTNAME','date','value','good','type'] # title
    # print(type(title))
    worksheet.write_row(col[0], title, format4)

    for i in range(len(data)):
        worksheet.write(i+1,0,data[i][0])
        worksheet.write(i+1,1,data[i][1])
        # worksheet.write(i+1,2,'{}'.format(str(data[i][2])))
        worksheet.write(i+1,2,data[i][2])
        worksheet.write(i+1,3,data[i][3])
        # worksheet.write(i+1,4,data[i][4])
    workbook.close()

# 将数据写入文件
def writeFile(data, fileName):
    with open(fileName, 'w+') as f:
        for line in data:
            s = ""
            for v in line:
                s = s + v + " "
            # print('s+v===>',s)
            # print(type(s))
            f.write(s.rstrip() + "\n")


if __name__ == '__main__':
    data = countlist()
    file_path = 'E:/sym/pi解析/PIF1y_interprolated_1y/DL-SW001-MMJCYX-1SJ-S-PLANTCONNECT.xlsx'
    write_excel_data(file_path,data)
    print('完成！！！')


'''
4.2-->6.0:
,result,    table,  _start,                         _stop,                          _time,                  _value,     AGPOINTNAME,        _field,     _table
,_result,   0,      2021-11-23T03:07:00.408151759Z, 2021-11-26T02:07:00.408151759Z, 2021-11-23T03:07:01Z,   true,       Simu1_1,            B,          test_table
,_result,   1,      2021-11-23T03:07:00.408151759Z, 2021-11-26T02:07:00.408151759Z, 2021-11-23T03:07:01Z,   8208,       Simu1_1,            state       test_table

[['0', '2014-12-16T08:57:30.609383307Z', '2021-12-16T02:57:30.609383307Z', '2021-11-26T02:48:37Z', '5467.76', 'Simu1_6', 'R', 'test_table', ''],
 ['1', '2014-12-16T08:57:30.609383307Z', '2021-12-16T02:57:30.609383307Z', '2021-11-26T02:48:37Z', '270352', 'Simu1_6', 'state', 'test_table', '']]

PI:
,result,    table,  _start,                         _stop,                              _time,                  _value,     AGPOINTNAME,                        _field,                 _table
,_result,   0,      2021-12-07T05:00:00.000000001Z, 2021-12-13T21:27:51.030181106Z,     2021-12-07T05:00:25Z,   50,         sy.st.WIN-F9KROVHMQ74.random1.sc1,  F,                      PI_TABLE
,_result,   1,      2021-12-07T05:00:00.000000001Z, 2021-12-13T21:27:51.030181106Z,     2021-12-07T05:00:25Z,   true,       sy.st.WIN-F9KROVHMQ74.random1.sc1,  Good,                   PI_TABLE

,result,    table,  _start,                          _stop,                             _time,                  _value,     AGPOINTNAME,                        _field,                  _table
,_result,   0,      2021-12-10T05:00:00.000000001Z,  2021-12-13T05:00:00.000000001Z,    2021-12-10T05:00:25Z,   true,       CDM158,                              Good,                  PI_TABLE
,_result,   1,      2021-12-10T05:00:00.000000001Z,  2021-12-13T05:00:00.000000001Z,    2021-12-10T05:00:25Z,   0,          CDM158,                              L,                     PI_TABLE

[['0', '2021-12-10T05:00:00.000000001Z', '2021-12-13T05:00:00.000000001Z', '2021-12-12T23:06:25Z', 'true', 'sy.st.WIN-F9KROVHMQ74.random1.DeviceStatus', 'Good', 'PI_TABLE', ''], 
 ['1', '2021-12-10T05:00:00.000000001Z', '2021-12-13T05:00:00.000000001Z', '2021-12-12T23:06:25Z', '0 | Good', 'sy.st.WIN-F9KROVHMQ74.random1.DeviceStatus', 'S', 'PI_TABLE']]
 

 
name,tags,      time,                   AGPOINTNAME,                    F,          Good,   L
PI,    ,        1642510804775009100,    DL-GH002-JYQNOX-4SJ-S-PI,       40.50433,   true,
PI,    ,        1642510814775009100,    DL-GH002-JYQNOX-4SJ-S-PI,       40.5599251, true,
PI,    ,        1642510819275009100,    DL-GH002-JYQNOX-4SJ-S-PI,       40.830246,  true,
PI,    ,        1642510824275009100,    DL-GH002-JYQNOX-4SJ-S-PI,       40.9119377, true,
 ['PI,,1642510804775009100,DL-GH002-JYQNOX-4SJ-S-PI,40.50433,true,
 \nPI,,1642510814775009100,DL-GH002-JYQNOX-4SJ-S-PI,40.5599251,true,
 \nPI,,1642510819275009100,DL-GH002-JYQNOX-4SJ-S-PI,40.830246,true,
 \nPI,,1642510824275009100,DL-GH002-JYQNOX-4SJ-S-PI,40.9119377,true,\n']
'''