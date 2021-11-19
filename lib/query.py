# coding=utf-8
import datetime
import string
import time

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
    re = re.replace('\r\n','').strip(',')
    lista  = []
    lista.append(re)
    print(lista)
    return re

def countlist():  ##获取查询接口的数据，并处理数据
    tq = test_QueryData()
    # tq = mockData()
    print(len(tq))
    listb = []
    for line in tq:
        # 获取AGPOINTNAME
        AGPOINTNAME = line[6]

        # 获取日期
        time = line[4]
        # 日期处理
        time = time.split('.')[0]
        time = time.replace('T',' ')

        #h获取value第一个值
        valueone = line[5]

        # 获取value第二个值
        valuetwo = line[5]
        v = '正常|好点'
        valuetwo = f'{v}{valuetwo}'

        # 写入浮点型
        datatype = f'浮点型r/R'

        # 获取日期数据
        # date = line[2]
        # # 截取日期数据
        # dateSub = date[0:string.rfind(date, '.')]
        # # 定义小时
        # eightHour = datetime.timedelta(hours=8)
        # # 将时间格式化为 datetime 类型
        # d = datetime.datetime.strptime(dateSub, '%Y-%m-%dT%H:%M:%S')
        # d = d + eightHour
        # f = datetime.datetime.strftime(d, '%Y-%m-%d %H:%M:%S')
        # row = [f]
        listb.append(AGPOINTNAME,time,valueone,valuetwo,datatype)

    print(listb)
    return listb


# 将数据写入文件
def writeFile(data, fileName):
    # f = open(fileName, 'w+')
    with open(fileName,'w+') as f:
        for line in data:
            f.write(json.dumps(line))



# 模拟数据
# def mockData():
#     mock = "[[\"_result\",0,\"2021-11-18T01:00:00.1634864721Z,3\"]]"
#     mockArr = json.loads(mock)
#     # print(mockArr)
#     # print(type(mockArr))
#     return mockArr


if __name__ == '__main__':
    test_QueryData()
    # fileName = "test.log"
    # data = countlist()
    # # mockData()
    # writeFile(data, fileName)
    # todo
