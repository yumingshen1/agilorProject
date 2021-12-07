# -*- coding: gbk -*-
import requests
import json
import xlrd, xlwt,openpyxl
import pandas as pd
import xlsxwriter

class parsingApi:
    # api��ҳ
    def home_api(self):
        res = requests.get('http://192.168.10.243:8080/piwebapi')
        data = res.json()['Links']['DataServers']
        str1 = data.split('/')[-1]
        return str1

    # ���ݿ�����
    def database_list(self):
        da = self.home_api()
        url = 'http://192.168.10.243:8080/piwebapi/'
        path = f'{url}{da}'
        res_list = requests.get(path)
        data = res_list.json()['Items'][0]['Links']['Points']
        str2 = data.split('dataservers/')[1]
        return str2

    # ���е���Ϣ
    @property           ##�����������ԣ����Ƿ����� ����ʱ��ֱ�ӵ��÷�������
    def information(self):
        da = self.database_list()
        url = 'http://192.168.10.243:8080/piwebapi/dataservers/'
        path = f'{url}{da}'     ## ƴ�����е���Ϣ

        some_list = requests.get(path)      ##��ȡ�����еĵ���Ϣ

        results_arr = []                    # ����һ��list�����������

        for item in some_list.json()['Items']:   ## ѭ������Ϣ
            name = item['Name']                     ## �������name
            name = name.replace(' ','')
            point_type = item['PointType']          ## ������� type
            if point_type == 'Float32':
                point_type = 'F'
            elif point_type == 'String':
                point_type = 'S'
            elif point_type == 'Int32':
                point_type = 'I'

            record_data = item['Links']['RecordedData']     #���InterpolatedData
            links = record_data.split('/streams/')[1]
            print('links-----------',links)
            starttime = '?startTime=2021-12-07T00:00:00.000Z'  ## ?startTime=2000-01-01T00:00:00Z&endTime=2022-01-01T00:00:00Z
            url = f'{"http://192.168.10.243:8080/piwebapi/streams/"}{links}{starttime}'  ## ƴ�Ӻ���ÿ��name��Ӧ��url
            print('url--------',url)
   # http://192.168.10.243:8080/piwebapi/streams/F1DPL9_f9XkRSkCpa9_eooJCywAwAAAAV0lOLUY5S1JPVkhNUTc0XFNZLlNULldJTi1GOUtST1ZITVE3NC5SQU5ET00xLkRFVklDRSBTVEFUVVM/recorded?startTime=2021-12-05T00:00:00.000Z
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
        # print("------excelд�����ݣ�{}".format(datas))
        # print("------excelд���ļ���{}".format(file_path))

        workbook = xlsxwriter.Workbook('{}'.format(file_path))  # �����ļ�
        worksheet = workbook.add_worksheet()  # ����sheet

        temp = 0   ##���������Ϊ�˱��values�������Ǽ���
        for index, item in enumerate(datas):  ## enumerate() �������ڽ�һ���ɱ��������ݶ������Ϊһ���������У�ͬʱ�г����ݺ������±꣬����ѭ�������datas[]
            if len(item['values']) == 0:    ## �ж������0����û�����б�
                index = index + temp        ##  �±� = �±�+���б�1+0��2+0��3+0
                worksheet.write(index, 0, '{}'.format(item['name']))
                worksheet.write(index, 1, '{}'.format(item['point_type']))
                worksheet.write(index, 2, '{}'.format(item['values'])) ## д����б�
            else:
                for ind, it in enumerate(item['values']): ## �ж�values��ֵ��� ��ѭ���±��ֵ
                    tm = index      ## ����±��������
                    if ind != 0:
                        ## �ڲ�values���±���0
                        temp = temp + 1     ## �ڲ�values����ֵ+1��ȡ����һ��Ԫ�أ��б�
                    index = index + temp    ## �ڲ�values���ݲ�ֹһ����index+1���൱��Excel����+1������һ��д��
                    # print("---it�� {}".format(it))
                    # print("---temp�� {}".format(temp))
                    # print("---index�� {}".format(index))

                    worksheet.write(index, 0, '{}'.format(item['name']))
                    worksheet.write(index, 2, '{}'.format(str(it[0])))
                    worksheet.write(index, 3, '{}'.format(str(it[1])))
                    worksheet.write(index, 4, '{}'.format(str(it[2])))
                    worksheet.write(index, 1, '{}'.format(item['point_type']))

                    index = tm  ## �������±� ��������index������ѭ����

        workbook.close()


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

    parsingApi().write_excel(parsingApi().information,'./data1.xlsx')

