# -*- coding: utf-8 -*-
# @Time: 2021/12/7 15:54
# @Author: shenyuming
# -*- coding: gbk -*-
import requests,datetime
import json
import xlrd, xlwt, openpyxl
import pandas as pd
import xlsxwriter,os
from utils.handle_path import report_path

"""
    pi 数据导出excel  --- 筛选点值
"""
class parsingApi:
    # 所有点信息
    @property  ##被声明是属性，不是方法， 调用时可直接调用方法本身
    def information(self):
        #直接请求点名字
        # path1 = 'http://192.168.30.72:8080/piwebapi/dataservers/F1DS3uSn5IfY2kGMucN6_OSrNAV0lOLVEzNzRQUEdBSDZD/points?nameFilter=sy.st.FWQ-DATAEX.PItoPI1.Scan%20Class%20Information'
        path1 = 'http://192.168.30.72:8080/piwebapi/dataservers/F1DS3uSn5IfY2kGMucN6_OSrNAV0lOLVEzNzRQUEdBSDZD/points?'  #?maxCount=45000
        some_list = requests.get(path1)  ##获取到所有的点信息
        print('samelist:',some_list)

        ## 定义需要的name
        need_name = ['CDM158']
        # 'sy.st.WIN-F9KROVHMQ74.random1.sc1','BA:LEVEL.1','CDM158','CDM1589','CDEP158','CDEP1589','sy.st.WIN-F9KROVHMQ74.random1.Device Status'

        results_arr = []  # 创建一个list存放所有数据

        for item in some_list.json()['Items']:  ## 循环点信息
            name = item['Name']  ## 获得所有name
            # print('name---%s,' %name)
            if name in need_name:
                name = name.replace(' ', '')
                point_type = item['PointType']  ## 获得所有 type
                if point_type == 'Float32':
                    point_type = 'F'
                elif point_type == 'String':
                    point_type = 'S'
                elif point_type == 'Int32':
                    point_type = 'I'
                elif point_type == 'Digital':
                    point_type = 'B'
                print('类型',point_type)
                '''
                    根据pi的实际情况来确定是需要获取RecordedData的数据还是InterpolatedData的数据
                '''
                record_data = item['Links']['RecordedData']  # 获得RecordedData
                Interpolated_data = item['Links']['InterpolatedData'] # 获得InterpolatedData
                links = Interpolated_data.split('/streams/')[1]
                # 定时时间范围、条数、插值的间隔
                starttime = '?startTime=2022-01-20T01:57:43.000Z'
                endtime = '&endTime=2022-02-06T08:25:56.000Z'
                num = '&maxCount=86400'
                t = '&interval=1y'  # 间隔
                url1 = f'{"http://192.168.30.72:8080/piwebapi/streams/"}{links}{starttime}{endtime}{t}{num}'
                print('url1------>',url1)

                ## 循环访问每个url1
                stream_datas = requests.get(url1).json()

                values = []  ##存放点的信息
                for v in stream_datas['Items']:  ##循环每个name请求的url后的数据
                    timestamp = v['Timestamp']  ## 时间直接获取
                    good = v['Good']  ## good直接获取
                    print('good--->',good)
                    if good == True:
                        good = 'true'
                    value = 0
                    if isinstance(v['Value'], dict):  ##判断请求的url中的 value 是不是字典类型  isinstance(object, classinfo)
                        if v['Value']['Value']:  ##如果是字典类型取value键下的value键的值
                            value = v['Value']['Value']  ## value取值
                    else:
                        value = v['Value']  ##value不是字典，直接取值

                    ##  时间处理
                    dateSub = timestamp[0:timestamp.rfind('.')]
                    # 定义小时
                    eightHour = datetime.timedelta(hours=8)
                    # 将时间格式化为 datetime 类型
                    d = datetime.datetime.strptime(dateSub, '%Y-%m-%dT%H:%M:%S')
                    d = d + eightHour
                    timestamp = datetime.datetime.strftime(d, '%Y-%m-%d %H:%M:%S')

                    r = [timestamp, value, good]  ## 将name 对应的一组 时间，value，good 存入一个list
                    # print('r---',r)
                    values.append(r)  ## 将每一个name 取得的 时间，value，good 放入一个list
                    # print('values----',values)

                row_dict = {'name': name, 'point_type': point_type,'values': values}  ##将 一个点的信息 name ,类型， 存放时间，value，good的list  全部 存入字典
                results_arr.append(row_dict)  ## 将存放每一个点的信息的 字典 放入list
                print("result_arr的值----->", results_arr)

                '''
                [{'name': 'sy.st.WIN-F9KROVHMQ74.random1.sc1', 'point_type': 'F', 'values': [['2021-12-07 13:00:25', 50.0, True], ['2021-12-07 13:00:55', 50.0, True]]}]
                '''
        return results_arr



    # 写入excel
    def write_excel(self, datas, file_path):

        workbook = xlsxwriter.Workbook('{}'.format(file_path))  # 建立文件
        worksheet = workbook.add_worksheet()  # 建立sheet

        tt = ['AGPOINTNAME', 'date', 'value', 'good', 'type']
        for index,item in enumerate(tt):
            worksheet.write(0,index,'{}'.format(item))

        temp = 0  ##定义变量，为了标记values的数据是几层
        for index, item in enumerate(datas):  ## enumerate() 函数用于将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标，这里循环传入的datas[]
            index = index+1
            if len(item['values']) == 0:  ## 判断如果是0或者没有子列表
                index = index + temp  ##  下标 = 下标+子列表，1+0，2+0，3+0
                worksheet.write(index, 0, '{}'.format(item['name']))
                worksheet.write(index, 1, '{}'.format(item['point_type']))
                worksheet.write(index, 2, '{}'.format(item['values']))  ## 写入空列表
            else:
                for ind, it in enumerate(item['values']):  ## 判断values有值情况 ，循环下标和值
                    tm = index  ## 外层下标存起来，
                    if ind != 0:
                        ## 内层values的下表不等0
                        temp = temp + 1  ## 内层values的数值+1，取第下一个元素（列表）
                    index = index + temp  ## 内层values数据不止一条，index+1（相当于Excel行数+1）向下一行写入
                    # print("---it： {}".format(it))
                    # print("---temp： {}".format(temp))
                    # print("---index： {}".format(index))

                    worksheet.write(index, 0, '{}'.format(item['name']))
                    worksheet.write(index, 1, '{}'.format(str(it[0])))
                    worksheet.write(index, 2, '{}'.format(str(it[1])))
                    worksheet.write(index, 3, '{}'.format(str(it[2])))
                    worksheet.write(index, 4, '{}'.format(item['point_type']))
                    index = tm  ## 将外层的下标 还给外层的index，继续循环，

        workbook.close()


 ## 写入文件
    def write_file(self, data_arr, file_name):
        with open(file_name, 'w+') as f:  ## 打开文件准备写入
            for line in data_arr:  ## 循环 information 函数返回的list ， list中每个字典代表一个点的信息 ， 循环时line就是一个字典
                print("Line的值--->", line)
                s = f"{line['name']} {line['point_type']}"  ## 写入取字典中的 name 和 类型
                if line['values']:  ## 判断列表values 正常或存在
                    for v in line['values']:  ## 循环values中的每一条数据
                        # print(type(v))
                        s1 = f" {v[0]} {v[1]} {v[2]}"  ## 取values中每一个字列表的0，1，2元素
                        f.write(s + s1 + "\n")


if __name__ == '__main__':
    file_path = os.path.join(report_path,'data.xlsx')
    file_path2 = 'E:/sym/pi解析/ABC.xlsx'
    parsingApi().write_excel(parsingApi().information, file_path2)

