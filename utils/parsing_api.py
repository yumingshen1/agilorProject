# -*- coding: gbk -*-
import requests
import json
import xlrd,xlwt

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
    def information(self):
        da = self.database_list()
        url = 'http://pi.vaiwan.com/piwebapi/dataservers/'
        path = f'{url}{da}'
        some_list = requests.get(path)

        name_list = []
        PointType_list = []
        RecordedData_list = []
        for i in range(len(some_list.json()['Items'])):
            name_list.append(some_list.json()['Items'][i]['Name'])
            PointType_list.append(some_list.json()['Items'][i]['PointType'])
            links = (some_list.json()['Items'][i]['Links']['RecordedData'])
            links = links.split('/streams/')[1]
            links = f'{"http://pi.vaiwan.com/piwebapi/streams/"}{links}'
            RecordedData_list.append(links)

        print(name_list,'\n',PointType_list,'\n',RecordedData_list)
        print(type(name_list))

        return name_list,PointType_list,RecordedData_list


    # 点的值
    def informationPage(self):
        da = self.information()



    # 写入
    def write_list(self,file_path,datas):
        f = xlwt.Workbook()
        sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
        # 将数据写入第 i 行，第 j 列
        i = 0
        for data in datas:
            for j in range(len(data)):
                sheet1.write(i, j, data[j])
            i = i + 1
        f.save(file_path)  # 保存文件
        # for i in range(len(data)):
        #     print(data[0])
        #     print(type(data))



if __name__ == '__main__':
    # parsingApi().home_api()
    # parsingApi().database_list()
    parsingApi().information()

    # data_list = parsingApi().information()
    # file_path = 'E:/sym/点值.xlsx'
    # parsingApi().write_list(file_path,data_list)