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
    @property
    def information(self):
        da = self.database_list()
        url = 'http://pi.vaiwan.com/piwebapi/dataservers/'
        path = f'{url}{da}'
        some_list = requests.get(path)

        results_arr = []

        for item in some_list.json()['Items']:
            name = item['Name']
            point_type = item['PointType']
            record_data = item['Links']['RecordedData']

            links = record_data.split('/streams/')[1]
            url = f'{"http://pi.vaiwan.com/piwebapi/streams/"}{links}'

            stream_datas = requests.get(url).json()

            values = []
            for v in stream_datas['Items']:
                timestamp = v['Timestamp']
                good = v['Good']
                value = 0
                if isinstance(v['Value'], dict):
                    if v['Value']['Value']:
                        value = v['Value']['Value']
                else:
                    value = v['Value']

                r = [timestamp, value, good]
                values.append(r)

            row_dict = {'name': name, 'point_type': point_type, 'values': values}
            results_arr.append(row_dict)

        return results_arr

    # 点的值
    def informationPage(self):
        da = self.information()
        print(da)
        for i in range(len(da)):
            pass


    # 写入
    def write_list(self, file_path, datas):
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

    def write_file(self, data_arr, file_name):
        with open(file_name, 'w+') as f:
            for line in data_arr:
                s = f"{line['name']} {line['point_type']}"
                if line['values']:
                    for v in line['values']:
                        print(type(v))
                        s1 = f"{v[0]} {v[1]} {v[2]}"
                        f.write(s + s1 + "\n")


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
