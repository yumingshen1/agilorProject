
from configs.config import HOST
from utils.handle_yml import get_yaml_data
import requests
import inspect

class baseApi:
    def __init__(self):
        ##通过模块名获得对应的数据
        # print(self.__class__.__name__)
        self.data = get_yaml_data('../configs/apiConfig.yml')[self.__class__.__name__]


    ## ----  公共方法------
    def request_send(self,data=None):
        methodName = inspect.stack()[1][3]  ##获取调用函数的名称
        print(type(methodName))
        print(self.data[methodName])
        print(type(self.data[methodName]))

        path = self.data[methodName]['path']
        print(path)
        print(type(path))

        method = self.data[methodName]['method']
        print(method)
        print(type(method))

        headers = self.data[methodName]['headers']
        print(headers)
        print(type(headers))

        # headerspath,method,heard = self.data[methodName].values()

        resp =requests.request(method=method,url=f'{HOST}{path}',headers=headers,data=data)

        return resp






