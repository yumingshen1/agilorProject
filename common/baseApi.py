
from configs.config import HOST
from utils.handle_yml import get_yaml_data
from utils.handle_path import config_path
import requests
import inspect
import os

class BaseApi:
    def __init__(self):
        ##通过模块名获得对应的数据
        # print(self.__class__.__name__)
        filepath = os.path.join(config_path,"apiConfig.yml")
        self.data = get_yaml_data(filepath)[self.__class__.__name__]
        # print(self.data)


    ## ----  公共方法------
    def request_send(self,data=None):
        try:
            methodName = inspect.stack()[1][3]  ##获取调用函数的名称
            # print(self.data[methodName])
            # print(type(self.data[methodName]))
            path = self.data[methodName]['path']
            method = self.data[methodName]['method']
            headers = self.data[methodName]['headers']
            url = f'{HOST}{path}'
            print(url)
            resp =requests.request(method=method,url=url,headers=headers,data=data)
            #
            return resp
        except Exception as e:
            print(e)
            raise e






