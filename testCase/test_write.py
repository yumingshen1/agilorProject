from common.baseApi import BaseApi
from configs.config import indata
from configs.config import payload
from utils.handle_yml import get_yaml_data
from utils.handle_path import config_path
import pytest
import os

class Wq(BaseApi):

    def write(self,data):
        respdata = self.request_send(data=data)   ##请求发送数据

        return respdata

    def query(self,quData):
        respon = self.request_send(data = quData)
        # print(respon.text)
        print(type(respon.text))

        return respon.text


    def pull_data(self):
        listdata = []

        pass

if __name__ == '__main__':
    print(Wq().write(indata))
    print(Wq().query(payload))