# -*- coding: gbk -*-
import requests
import json
import xlrd, xlwt


class parsingApi:
    # api首页
    def home_api(self):
        res = requests.get('http://pi.vaiwan.com/piwebapi/')
        data = res.json()['Links']['DataServers']
        str1 = data.split('/')[-1]
        return str1

    # 数据库连接
    def database_list(self):
        da = self.home_api()
        url = 'http://pi.vaiwan.com/piwebapi/'
        path = f'{url}{da}'
        res_list = requests.get(path)
        data = res_list.json()['Items'][0]['Links']['Points']
        str2 = data.split('dataservers/')[1]
        return str2

    # 所有点信息
    @property           ##被声明是属性，不是方法， 调用时可直接调用方法本身
    def information(self):
        da = self.database_list()
        url = 'http://pi.vaiwan.com/piwebapi/dataservers/'
        path = f'{url}{da}'
        some_list = requests.get(path)      ##获取到所有的点信息

        results_arr = []                    # 创建一个list存放所有数据

        for item in some_list.json()['Items']:   ## 循环点信息
            name = item['Name']                     ## 获得所有name
            point_type = item['PointType']          ## 获得所有 type
            record_data = item['Links']['RecordedData']     #获得InterpolatedData
            links = record_data.split('/streams/')[1]
            url = f'{"http://pi.vaiwan.com/piwebapi/streams/"}{links}'  ## 拼接后获得每个name对应的url

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
                print("r的值----->",r)
                values.append(r)                       ## 将每一个name 取得的 时间，value，good 放入一个list
                print("values的值----->",values)

            row_dict = {'name': name, 'point_type': point_type, 'values': values}    ##将 一个点的信息 name ,类型， 存放时间，value，good的list  全部 存入字典
            print("row_dict的值----->",row_dict)
            results_arr.append(row_dict)                            ## 将存放每一个点的信息的 字典 放入list
            print("result_arr的值----->",results_arr)
        return results_arr


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

 # 写入
    def write_excel(self, file_path, datas):
        f = xlwt.Workbook()
        sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
        # 将数据写入第 i 行，第 j 列
        i = 0
        for data in datas:
            for j in range(len(data)):
                sheet1.write(i, j, data[j])
            i = i + 1
        f.save(file_path)  # 保存文件

if __name__ == '__main__':
    # parsingApi().home_api()
    # parsingApi().database_list()
    # parsingApi().information()
    # parsingApi().informationPage()
    # print(type(parsingApi().informationPage()))
    # data_list = parsingApi().information()
    # file_path = 'E:/sym/点值.xlsx'
    # parsingApi().write_list(file_path,data_list)
    parsingApi().write_file(parsingApi().information, 'test2.log')