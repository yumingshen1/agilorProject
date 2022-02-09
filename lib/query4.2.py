# coding=utf-8
import array
import datetime
import string
import time
import xlwt,xlsxwriter
import numpy as np
import requests
import json

"""
    迁移4.2数据到6.2数据库后导出数据库的数据到excel, 
"""

def test_QueryData():  ##查询接口
    url = "http://192.168.220.150:8713/agilorapi/v6/query"
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
    print('respone的返回---->',response.text)

    re = response.text.replace(',result,table,_start,_stop,_time,_value,AGPOINTNAME,_field,_table','')

    re = re.replace('\r\n', '').strip(',')
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
    for index, v in timeMap.items():
        Simu1 = v[0][5]
        date = v[0][3]
        # 处理时间
        dateSub = date[0:date.rfind('.')]
        # 定义小时
        eightHour = datetime.timedelta(hours=8)
        # 将时间格式化为 datetime 类型
        d = datetime.datetime.strptime(dateSub, '%Y-%m-%dT%H:%M:%S')
        d = d + eightHour
        df = datetime.datetime.strftime(d, '%Y-%m-%d %H:%M:%S')

        type = v[0][6]
        if type in ('R','B','L','S'):
            value1 = v[0][4]
            value2 = ""
            if v[1]:
                value2 = v[1][4]
            print('v====>',v)
            param = f'{statusStr}{" "}{value2}'
        else:
            value1 = v[1][4]
            param = v[0][4]
            type = v[1][6]

        if type == 'R':
            type = '浮点型r/R'
        elif type == 'B':
            type = '布尔型b/B'
        elif type == 'L':
            type = '长整型l/L'
        elif type == 'S':
            type = '字符串型s/S'

        row = [Simu1, df, value1,param, type]
        listb.append(row)
    print('listb数据',listb)
    # [['Simu1_1', '2021-11-26 10:48:37', 'true', '8208', '布尔型b/B'], ['Simu1_1', '2021-11-26 10:48:38', 'true', '8208', '布尔型b/B']]
    return listb

# 解析数据转为数组，去掉_result
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
    ## 添加表头
    format4 = workbook.add_format(
        {'font_size': '12', 'align': 'center', 'valign': 'vcenter', 'bold': True, 'font_color': '#217346',
         'bg_color': '#FFD1A4'})
    col = ['A1', 'B1', 'C1', 'D1', 'E1']
    title = [u'AGPOINTNAME','date','value1','value2','type'] # title
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
            print('s+v===>',s)
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
    file_path = 'E:/sym/4.2迁移/导出6.0数据_linux/sium1_6.xlsx'
    write_excel_data(file_path,data)