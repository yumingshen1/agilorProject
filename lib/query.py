# coding=utf-8
import datetime
import string
import time

import requests
import json


def test_QueryData():  ##查询接口
    url = "http://192.168.220.134:8713/agilorapi/v6/query"
    payload = json.dumps({
        "db": "agilor_test",
        "start": "2021-11-18T08:51:00.1634864721Z",
        "table": "cpu_usage_func11",
        "tags": [
            {
                "AGPOINTNAME": "Simu1_1"
            }
        ]
    })

    headers = {
        'Authorization': 'Token XXX',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    print(type(response.text))  ##查询后得到str类型的多条数据
    return response


def countlist():  ##获取查询接口的数据，并处理数据
    # tq = test_QueryData()
    tq = mockData()
    # print(len(tq)
    list = []
    for line in tq:
        # todo 获取其他值

        # 获取日期数据
        date = line[2]
        # 截取日期数据
        dateSub = date[0:string.rfind(date, '.')]
        # 定义小时
        eightHour = datetime.timedelta(hours=8)
        # 将时间格式化为 datetime 类型
        d = datetime.datetime.strptime(dateSub, '%Y-%m-%dT%H:%M:%S')
        d = d + eightHour
        f = datetime.datetime.strftime(d, '%Y-%m-%d %H:%M:%S')
        row = [f]
        list.append(row)

    print(list)
    return list

# 将数据写入文件
def writeFile(data, fileName):
    f = open(fileName, 'w+')

    for line in data:
        #todo 这里是已json 格式写入，其他格式自行组合
        f.write(json.dumps(line))

    f.close()

# 模拟数据
def mockData():
    mock = "[[\"_result\",0,\"2021-11-18T01:00:00.1634864721Z,3\"]]"
    mockArr = json.loads(mock)
    return mockArr


if __name__ == '__main__':
    # test_QueryData()
    fileName = "test.log"
    data = countlist()
    # mockData()
    writeFile(data, fileName)
