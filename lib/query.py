# coding=utf-8
import array
import datetime
import string
import time

import numpy as np
import requests
import json


def test_QueryData():  ##查询接口
    url = "http://192.168.220.134:8713/agilorapi/v6/query"
    data = {
        "db": "agilor_test",
        "start": "2021-11-19T01:01:00.1634864721Z",
        "table": "cpu_usage_func11",
        "tags": [
            {
                "AGPOINTNAME": "Simu1_1"
            }
        ]
    }
    headers = {
        'Authorization': 'Token XXX',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.text)
    re = response.text.split('_table')[1]
    print(re)
    re = re.replace('\r\n', '').strip(',')
    lista = []
    lista.append(re)
    print(lista)
    return re


def takeSecond(elem):
    return elem[0][0], elem[1][0]


def countlist():  ##获取查询接口的数据，并处理数据
    tq = test_QueryData()
    # tq = mockData()
    tq = resolver(tq)
    print(len(tq))
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

    statusStr = "正常|好点"
    s = "浮点型r/R"
    for index, v in timeMap.items():
        # print(v[0])
        Simu1_1 = v[0][5]
        date = v[0][3]
        param1 = v[0][4]
        param2 = ""
        if v[1]:
            param2 = v[1][4]

        dateSub = date[0:date.rfind('.')]
        # 定义小时
        eightHour = datetime.timedelta(hours=8)
        # 将时间格式化为 datetime 类型
        d = datetime.datetime.strptime(dateSub, '%Y-%m-%dT%H:%M:%S')
        d = d + eightHour
        df = datetime.datetime.strftime(d, '%Y-%m-%d %H:%M:%S')

        row = [Simu1_1, df, param2, statusStr, param1, s]
        listb.append(row)

    return listb


# 将数据写入文件
def writeFile(data, fileName):
    with open(fileName, 'w+') as f:
        for line in data:
            s = ""
            for v in line:
                s = s + v + " "
            f.write(s.rstrip() + "\n")


# 解析数据转为数组
def resolver(data):
    # dataArr = string.split(data, ",_result,")
    dataArr = data.split("_result,")
    dataArr.pop(0)
    for line in dataArr:
        print(line)
    # print("----------")
    return dataArr


# 模拟数据
# def mockData():
#     mock = ",result,table,_start,_stop,_time,_value,AGPOINTNAME,_field,_table" \
#            ",_result,1,2021-11-19T01:01:00.163486472Z,2021-11-19T04:51:19.648740986Z,2021-11-19T01:59:29.255251114Z,666.1234,Simu1_1,wendu,cpu_usage_func11" \
#            ",_result,0,2021-11-19T01:01:00.163486472Z,2021-11-19T04:51:19.648740986Z,2021-11-19T01:59:29.255251114Z,8208,Simu1_1,status,cpu_usage_func11" \
#            ",_result,0,2021-11-19T01:01:00.163486472Z,2021-11-19T04:51:19.648740986Z,2021-11-19T03:39:13.295111728Z,8208,Simu1_1,status,cpu_usage_func11" \
#            ",_result,1,2021-11-19T01:01:00.163486472Z,2021-11-19T04:51:19.648740986Z,2021-11-19T03:39:13.295111728Z,677.1234,Simu1_1,wendu,cpu_usage_func11"
#
#     return mock


if __name__ == '__main__':
    # mockData = mockData()
    # resolver(mockData)
    # test_QueryData()
    fileName = "test.log"
    data = countlist()
    writeFile(data, fileName)
