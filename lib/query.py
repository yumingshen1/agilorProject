# coding=utf-8
import array
import datetime
import string
import time

import numpy as np
import requests
import json

# agilor_migration test_table
def test_QueryData():  ##查询接口
    url = "http://192.168.220.134:8713/agilorapi/v6/query"
    data = {
        "db": "agilor_migration",
        "start": "-7y",
        "table": "test_table",
        "tags": [
            {
                "AGPOINTNAME": "Simu1_6"
            }
        ]
    }
    headers = {
        'Authorization': 'Token XXX',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(type(response.text))
    print('respone的返回---->',response.text)

    re = response.text.replace(',result,table,_start,_stop,_time,_value,AGPOINTNAME,_field,_table','')
    # re = response.text.split(',result,table,_start,_stop,_time,_value,AGPOINTNAME,_field,_table')[1]
    print('第一次切割：----->',re)

    re = re.replace('\r\n', '').strip(',')
    lista = []
    lista.append(re)
    print('lista添加的结果---->',lista)
    return re
'''
,result,table,_start,_stop,_time,_value,AGPOINTNAME,_field,_table
,_result,0,2021-11-23T03:07:00.408151759Z,2021-11-26T02:07:00.408151759Z,2021-11-23T03:07:01Z,true,Simu1_1,B,test_table
,_result,0,2021-11-23T03:07:00.408151759Z,2021-11-26T02:07:00.408151759Z,2021-11-23T03:07:02Z,true,Simu1_1,B,test_table

,result,table,_start,_stop,_time,_value,AGPOINTNAME,_field,_table
,_result,1,2021-11-23T03:07:00.408151759Z,2021-11-26T02:07:00.408151759Z,2021-11-23T03:07:01Z,8208,Simu1_1,state,test_table
,_result,1,2021-11-23T03:07:00.408151759Z,2021-11-26T02:07:00.408151759Z,2021-11-23T03:07:02Z,8208,Simu1_1,state,test_table
'''

def takeSecond(elem):
    return elem[0][0], elem[1][0]


def countlist():  ##获取查询接口的数据，并处理数据
    tq = test_QueryData()
    # tq = mockData()
    tq = resolver(tq)
    # print(len(tq))
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
    s = "浮点型r/R"
    for index, v in timeMap.items():
        # print(v[0])
        Simu1_1 = v[0][5]              ## simu1
        date = v[0][3]                 # 时间
        param1 = v[0][4]                ## 8208---> 变为true 或 false  数字
        type = v[0][6]                  ##  类型
        param2 = ""                     ## 变为8208值
        if v[1]:
            param2 = v[1][4]
        print('v====>',v)
        print('v[0]===>',v[0])
        print('v[1]===>',v[1])
        dateSub = date[0:date.rfind('.')]
        # 定义小时
        eightHour = datetime.timedelta(hours=8)
        # 将时间格式化为 datetime 类型
        d = datetime.datetime.strptime(dateSub, '%Y-%m-%dT%H:%M:%S')
        d = d + eightHour
        df = datetime.datetime.strftime(d, '%Y-%m-%d %H:%M:%S')
        param3 = f'{statusStr}{param2}'
        row = [Simu1_1, df, param1,param2, s]
        listb.append(row)
    print('listb数据',listb)
    return listb


# 将数据写入文件
def writeFile(data, fileName):
    with open(fileName, 'w+') as f:
        for line in data:
            s = ""
            for v in line:
                s = s + v + " "
            print('s+v===>',s)
            # print(type(s))
            f.write(s.rstrip() + "\n")

import xlwt
## 数据写入excel
def write_excel_data(data):
    # listc = data
    output = open('E:/sym/4.2迁移/66.xlsx', 'w+', encoding='gbk')
    output.write('AGPOINTNAME\tdate\tnumerical\tnum\ttype\n')
    for i in range(len(data)):
        for j in range(len(data[i])):
            output.write(str(data[i][j]))  # write函数不能写int类型的参数，所以使用str()转化
            output.write('\t')  # 相当于Tab一下，换一个单元格
        output.write('\n')  # 写完一行立马换行
    output.close()



# 解析数据转为数组
def resolver(data):
    # dataArr = string.split(data, ",_result,")
    dataArr = data.split("_result,")
    dataArr.pop(0)
    for line in dataArr:
        print(line)
    # print("----------")
    return dataArr


# # 模拟数据
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
    fileName = "test3.log"
    fileExcel = "excel_b"
    data = countlist()
    # writeFile(data, fileName)
    write_excel_data(data)