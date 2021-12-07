# -*- coding: gbk -*-
import requests
import json
import xlrd, xlwt,openpyxl
import pandas as pd
import xlsxwriter

class parsingApi:
    # api首页
    def home_api(self):
        res = requests.get('http://192.168.10.243:8080/piwebapi')
        data = res.json()['Links']['DataServers']
        str1 = data.split('/')[-1]
        return str1

    # 数据库连接
    def database_list(self):
        da = self.home_api()
        url = 'http://192.168.10.243:8080/piwebapi/'
        path = f'{url}{da}'
        res_list = requests.get(path)
        data = res_list.json()['Items'][0]['Links']['Points']
        str2 = data.split('dataservers/')[1]
        return str2

    # 所有点信息
    @property           ##被声明是属性，不是方法， 调用时可直接调用方法本身
    def information(self):
        da = self.database_list()
        url = 'http://192.168.10.243:8080/piwebapi/dataservers/'
        path = f'{url}{da}'     ## 拼接所有点信息

        some_list = requests.get(path)      ##获取到所有的点信息

        results_arr = []                    # 创建一个list存放所有数据

        for item in some_list.json()['Items']:   ## 循环点信息
            name = item['Name']                     ## 获得所有name
            name = name.replace(' ','')
            point_type = item['PointType']          ## 获得所有 type
            if point_type == 'Float32':
                point_type = 'F'
            elif point_type == 'String':
                point_type = 'S'
            elif point_type == 'Int32':
                point_type = 'I'

            record_data = item['Links']['RecordedData']     #获得InterpolatedData
            links = record_data.split('/streams/')[1]
            print('links-----------',links)
            starttime = '?startTime=2021-12-07T00:00:00.000Z'  ## ?startTime=2000-01-01T00:00:00Z&endTime=2022-01-01T00:00:00Z
            url = f'{"http://192.168.10.243:8080/piwebapi/streams/"}{links}{starttime}'  ## 拼接后获得每个name对应的url
            print('url--------',url)
   # http://192.168.10.243:8080/piwebapi/streams/F1DPL9_f9XkRSkCpa9_eooJCywAwAAAAV0lOLUY5S1JPVkhNUTc0XFNZLlNULldJTi1GOUtST1ZITVE3NC5SQU5ET00xLkRFVklDRSBTVEFUVVM/recorded?startTime=2021-12-05T00:00:00.000Z
            stream_datas = requests.get(url).json()     ## 循环访问每个url

            values = []
            for v in stream_datas['Items']:     ##循环每个name请求的url后的数据
                timestamp = v['Timestamp']      ## 时间直接获取
                good = v['Good']                ## good直接获取
                value = 0
                if isinstance(v['Value'], dict): ##判断请求的url中的 value 是不是字典类型
                    if v['Value']['Value']:         ##如果是字典类型取value键下的value键的值
                        value = v['Value']['Value']     ## value取值
                else:
                    value = v['Value']      ##value不是字典，直接取值

                r = [timestamp, value, good]           ## 将name 对应的一组 时间，value，good 存入一个list
                # print("r的值----->",r)
                values.append(r)                       ## 将每一个name 取得的 时间，value，good 放入一个list
                # print("values的值----->",values)

            row_dict = {'name': name, 'point_type': point_type, 'values': values}    ##将 一个点的信息 name ,类型， 存放时间，value，good的list  全部 存入字典
            # print("row_dict的值----->",row_dict)
            results_arr.append(row_dict)                            ## 将存放每一个点的信息的 字典 放入list
            # print("result_arr的值----->",results_arr)
        return results_arr
## 返回数据格式 [{'name': '111111', 'point_type': 'Float32', 'values': [['2021-12-02T09:28:01Z', 50.0, True], ['2021-12-02T17:28:01Z', 50.0, True], ['2021-12-03T01:28:01Z', 50.0, True], ['2021-12-03T02:28:01Z', 50.0, True]]}, {'name': 'sy.st.WIN-F9KROVHMQ74.random1.Device Status', 'point_type': 'String', 'values': [['2021-12-02T08:11:31Z', '0 | Good', True], ['2021-12-02T16:11:31Z', '0 | Good', True], ['2021-12-03T00:11:31Z', '0 | Good', True]]}]

    ## 写入文件
    def write_file(self, data_arr, file_name):
        with open(file_name, 'w+') as f:            ## 打开文件准备写入
            for line in data_arr:                  ## 循环 information 函数返回的list ， list中每个字典代表一个点的信息 ， 循环时line就是一个字典
                print("Line的值--->",line)
                s = f"{line['name']} {line['point_type']}"    ## 写入取字典中的 name 和 类型
                if line['values']:                          ## 判断列表values 正常或存在
                    for v in line['values']:               ## 循环values中的每一条数据
                        # print(type(v))
                        s1 = f" {v[0]} {v[1]} {v[2]}"       ## 取values中每一个字列表的0，1，2元素
                        f.write(s + s1 + "\n")

 # 写入excel
    def write_excel(self,datas,file_path):
        # print("------excel写入数据：{}".format(datas))
        # print("------excel写入文件：{}".format(file_path))

        workbook = xlsxwriter.Workbook('{}'.format(file_path))  # 建立文件
        worksheet = workbook.add_worksheet()  # 建立sheet

        temp = 0   ##定义变量，为了标记values的数据是几层
        for index, item in enumerate(datas):  ## enumerate() 函数用于将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标，这里循环传入的datas[]
            if len(item['values']) == 0:    ## 判断如果是0或者没有子列表
                index = index + temp        ##  下标 = 下标+子列表，1+0，2+0，3+0
                worksheet.write(index, 0, '{}'.format(item['name']))
                worksheet.write(index, 1, '{}'.format(item['point_type']))
                worksheet.write(index, 2, '{}'.format(item['values'])) ## 写入空列表
            else:
                for ind, it in enumerate(item['values']): ## 判断values有值情况 ，循环下标和值
                    tm = index      ## 外层下标存起来，
                    if ind != 0:
                        ## 内层values的下表不等0
                        temp = temp + 1     ## 内层values的数值+1，取第下一个元素（列表）
                    index = index + temp    ## 内层values数据不止一条，index+1（相当于Excel行数+1）向下一行写入
                    # print("---it： {}".format(it))
                    # print("---temp： {}".format(temp))
                    # print("---index： {}".format(index))

                    worksheet.write(index, 0, '{}'.format(item['name']))
                    worksheet.write(index, 2, '{}'.format(str(it[0])))
                    worksheet.write(index, 3, '{}'.format(str(it[1])))
                    worksheet.write(index, 4, '{}'.format(str(it[2])))
                    worksheet.write(index, 1, '{}'.format(item['point_type']))

                    index = tm  ## 将外层的下标 还给外层的index，继续循环，

        workbook.close()


if __name__ == '__main__':
    # parsingApi().home_api()
    # parsingApi().database_list()
    # parsingApi().information()
    # parsingApi().informationPage()
    # print(type(parsingApi().informationPage()))
    # data_list = parsingApi().information()
    # file_path = 'E:/sym/点值.xlsx'
    # parsingApi().write_list(file_path,data_list)

    # parsingApi().write_file(parsingApi().information, 'test2.log')

    parsingApi().write_excel(parsingApi().information,'./data1.xlsx')

