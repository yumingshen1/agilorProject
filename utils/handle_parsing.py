# -*- coding: gbk -*-
import requests
import json
import xlrd, xlwt,openpyxl
import pandas as pd

class parsingApi:
    # api��ҳ
    def home_api(self):
        res = requests.get('http://pi.vaiwan.com/piwebapi/')
        data = res.json()['Links']['DataServers']
        str1 = data.split('/')[-1]
        return str1

    # ���ݿ�����
    def database_list(self):
        da = self.home_api()
        url = 'http://pi.vaiwan.com/piwebapi/'
        path = f'{url}{da}'
        res_list = requests.get(path)
        data = res_list.json()['Items'][0]['Links']['Points']
        str2 = data.split('dataservers/')[1]
        return str2

    # ���е���Ϣ
    @property           ##�����������ԣ����Ƿ����� ����ʱ��ֱ�ӵ��÷�������
    def information(self):
        da = self.database_list()
        url = 'http://pi.vaiwan.com/piwebapi/dataservers/'
        path = f'{url}{da}'
        some_list = requests.get(path)      ##��ȡ�����еĵ���Ϣ

        results_arr = []                    # ����һ��list�����������

        for item in some_list.json()['Items']:   ## ѭ������Ϣ
            name = item['Name']                     ## �������name
            point_type = item['PointType']          ## ������� type
            record_data = item['Links']['RecordedData']     #���InterpolatedData
            links = record_data.split('/streams/')[1]
            url = f'{"http://pi.vaiwan.com/piwebapi/streams/"}{links}'  ## ƴ�Ӻ���ÿ��name��Ӧ��url

            stream_datas = requests.get(url).json()     ## ѭ������ÿ��url

            values = []
            for v in stream_datas['Items']:     ##ѭ��ÿ��name�����url�������
                timestamp = v['Timestamp']      ## ʱ��ֱ�ӻ�ȡ
                good = v['Good']                ## goodֱ�ӻ�ȡ
                value = 0
                if isinstance(v['Value'], dict): ##�ж������url�е� value �ǲ����ֵ�����
                    if v['Value']['Value']:         ##������ֵ�����ȡvalue���µ�value����ֵ
                        value = v['Value']['Value']     ## valueȡֵ
                else:
                    value = v['Value']      ##value�����ֵ䣬ֱ��ȡֵ

                r = [timestamp, value, good]           ## ��name ��Ӧ��һ�� ʱ�䣬value��good ����һ��list
                # print("r��ֵ----->",r)
                values.append(r)                       ## ��ÿһ��name ȡ�õ� ʱ�䣬value��good ����һ��list
                # print("values��ֵ----->",values)

            row_dict = {'name': name, 'point_type': point_type, 'values': values}    ##�� һ�������Ϣ name ,���ͣ� ���ʱ�䣬value��good��list  ȫ�� �����ֵ�
            # print("row_dict��ֵ----->",row_dict)
            results_arr.append(row_dict)                            ## �����ÿһ�������Ϣ�� �ֵ� ����list
            # print("result_arr��ֵ----->",results_arr)
        return results_arr
## �������ݸ�ʽ [{'name': '111111', 'point_type': 'Float32', 'values': [['2021-12-02T09:28:01Z', 50.0, True], ['2021-12-02T17:28:01Z', 50.0, True], ['2021-12-03T01:28:01Z', 50.0, True], ['2021-12-03T02:28:01Z', 50.0, True]]}, {'name': 'sy.st.WIN-F9KROVHMQ74.random1.Device Status', 'point_type': 'String', 'values': [['2021-12-02T08:11:31Z', '0 | Good', True], ['2021-12-02T16:11:31Z', '0 | Good', True], ['2021-12-03T00:11:31Z', '0 | Good', True]]}]

    ## д���ļ�
    def write_file(self, data_arr, file_name):
        with open(file_name, 'w+') as f:            ## ���ļ�׼��д��
            for line in data_arr:                  ## ѭ�� information �������ص�list �� list��ÿ���ֵ����һ�������Ϣ �� ѭ��ʱline����һ���ֵ�
                print("Line��ֵ--->",line)
                s = f"{line['name']} {line['point_type']}"    ## д��ȡ�ֵ��е� name �� ����
                if line['values']:                          ## �ж��б�values ���������
                    for v in line['values']:               ## ѭ��values�е�ÿһ������
                        # print(type(v))
                        s1 = f" {v[0]} {v[1]} {v[2]}"       ## ȡvalues��ÿһ�����б��0��1��2Ԫ��
                        f.write(s + s1 + "\n")

 # д��excel
    def write_excel(self,datas,file_path):
        with open(file_path,'w+') as f:
            for i in datas:
                name = i['name']
                type = i['point_type']
                print('i��ֵ--->',i)
                print('name��ֵ---->',name)
                print('type��ֵ---->',type)
                if i['values']:
                    for v in i['values']:
                        time = v[0]
                        va = v[1]
                        go = v[2]
                        print('time��ֵ---->', time)
                        print('va��ֵ---->', va)
                        print('go��ֵ---->', go)


        # wb = openpyxl.Workbook()
        # sheet = wb.active
        # sheet.title = "Sheet1"
        # sheet['A1'].value = 'name'
        # sheet['B1'].value = 'point_type'
        # j = 1
        # for item in datas:
        #     sheet['A' + str(j)].value = item['name']
        #     sheet['B' + str(j)].value = item['point_type']
        #     j = j + 1
        # wb.save(file_path)
        # print('������ɣ�����')

'''
 output.write('AGPOINTNAME\tdate\tnumerical\tnum\ttype\n')
    for i in range(len(data)):
        for j in range(len(data[i])):
            output.write(str(data[i][j]))  # write��������дint���͵Ĳ���������ʹ��str()ת��
            output.write('\t')  # �൱��Tabһ�£���һ����Ԫ��
        output.write('\n')  # д��һ��������
    output.close()
'''




if __name__ == '__main__':
    # parsingApi().home_api()
    # parsingApi().database_list()
    # parsingApi().information()
    # parsingApi().informationPage()
    # print(type(parsingApi().informationPage()))
    # data_list = parsingApi().information()
    # file_path = 'E:/sym/��ֵ.xlsx'
    # parsingApi().write_list(file_path,data_list)

    # parsingApi().write_file(parsingApi().information, 'test2.log')

    parsingApi().write_excel(parsingApi().information,'./data.xlsx')