# -*- coding: gbk -*-
import requests
import json

class parsingApi:

    def home_api(self):
        res = requests.get('http://pi.vaiwan.com/piwebapi/')
        data = res.json()['Links']['DataServers']
        str1 = data.split('/')[-1]
        return str1

    def database_list(self):
        da = self.home_api()
        url = 'http://pi.vaiwan.com/piwebapi/'
        path = f'{url}{da}'
        res_list = requests.get(path)
        data = res_list.json()['Items'][0]['Links']['Points']
        str2 = data.split('dataservers/')[1]
        return str2

    def information(self):
        da = self.database_list()
        url = 'http://pi.vaiwan.com/piwebapi/dataservers/'
        path = f'{url}{da}'
        some_list = requests.get(path)
        print(type(some_list.json()))
        # print(some_list.json()['Items'])
        name_list = []
        PointType_list = []
        WebId = []
        for i in range(len(some_list.json()['Items'])):
            name_list.append(some_list.json()['Items'][i]['Name'])
            PointType_list.append(some_list.json()['Items'][i]['PointType'])
            WebId.append(some_list.json()['Items'][i]['WebId'])
        print(name_list)
        print(PointType_list)
        print(WebId)



    def informationPage(self):
        url = 'http://pi.vaiwan.com/piwebapi/streams/'




if __name__ == '__main__':
    # parsingApi().home_api()
    # parsingApi().database_list()
    parsingApi().information()