# coding=utf-8
import array
import datetime
import string
import time
import xlwt,xlsxwriter
import numpy as np
import requests
import json

def test_QueryData():  ##查询接口
    url = "http://192.168.220.150:8713/agilorapi/v6/query"
    data = {
        "db": "PI",
        "start": "2021-12-10T05:00:00.000000001Z",
        "stop": "2021-12-13T05:00:00.000000001Z",
        "table": "PI_TABLE",
        "tags": [
            {
                "AGPOINTNAME":"sy.st.WIN-F9KROVHMQ74.random1.DeviceStatus"
            }
        ]
    }
    headers = {
        'Authorization': 'Token XXX',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    # print(type(response.text))

    re = response.text.replace(',result,table,_start,_stop,_time,_value,AGPOINTNAME,_field,_table','')

    re = re.replace('\r\n', '').strip(',')
    lista = []
    lista.append(re)
    # print('lista添加的结果---->',lista)
    return re

def countlist():  ##获取查询接口的数据，并处理数据
    tq = test_QueryData()
    tq = resolver(tq)
    listb = []
    timeMap = {}

    # 对数据根据时间进行分组
    for l in tq:
        arr = l.split(",")
        lastTime = arr[3]
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

    statusStr = "正常|好点"     ## 不需要了
    # s = "浮点型r/R"
    for index, v in timeMap.items():
        AGPOINTNAME = v[0][5]
        date = v[0][3]
        dateSub = date[0:date.rfind('.')]
        # 定义小时
        eightHour = datetime.timedelta(hours=8)
        # 将时间格式化为 datetime 类型
        d = datetime.datetime.strptime(dateSub, '%Y-%m-%dT%H:%M:%S')
        d = d + eightHour
        df = datetime.datetime.strftime(d, '%Y-%m-%d %H:%M:%S')

        type = v[0][6]
        if type in ('F','L','B','S'):
            value = v[0][4]
            good = ""
            if v[1]:
                good = v[1][4]
            print('v====>',v)
            # print('v[0]===>',v[0])
            # print('v[1]===>',v[1])
        else:
            value = v[1][4]
            good = v[0][4]
            type = v[1][6]
        row = [AGPOINTNAME, df, value,good, type]
        listb.append(row)
        # print('listb数据',listb)
    return listb

# 解析数据转为数组 ，去除_result
def resolver(data):
    dataArr = data.split("_result,")
    dataArr.pop(0)
    return dataArr

## 数据写入excel
def write_excel_data(filepath,data):
    now = datetime.datetime.now().strftime('%Y-%m-%d')  # 当前时间
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
        worksheet.write(i+1,2,'{}'.format(str(data[i][2])))
        worksheet.write(i+1,3,data[i][3])
        worksheet.write(i+1,4,data[i][4])
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

# 模拟数据
def mockData():
    mock = ",result,table,_start,_stop,_time,_value,AGPOINTNAME,_field,_table" \
           ",_result,1,2021-11-19T01:01:00.163486472Z,2021-11-19T04:51:19.648740986Z,2021-11-19T01:59:29.255251114Z,666.1234,Simu1_1,wendu,cpu_usage_func11" \
           ",_result,0,2021-11-19T01:01:00.163486472Z,2021-11-19T04:51:19.648740986Z,2021-11-19T01:59:29.255251114Z,8208,Simu1_1,status,cpu_usage_func11" \
           ",_result,0,2021-11-19T01:01:00.163486472Z,2021-11-19T04:51:19.648740986Z,2021-11-19T03:39:13.295111728Z,8208,Simu1_1,status,cpu_usage_func11" \
           ",_result,1,2021-11-19T01:01:00.163486472Z,2021-11-19T04:51:19.648740986Z,2021-11-19T03:39:13.295111728Z,677.1234,Simu1_1,wendu,cpu_usage_func11"

    return mock


if __name__ == '__main__':
    data = countlist()
    file_path = 'E:/sym/pi解析/pi_post_linux/rtdb_DeviceStatus.xlsx'
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
'''