from common.baseApi import BaseApi
from configs.config import indata
from configs.config import payload
from utils.handle_yml import get_yaml_data,get_yaml_data2
from utils.handle_path import config_path
import pytest
import os
from lib.wrqu import Wq

class Testag:
    # dataymlfile = os.path.join(config_path,'writeData.yml')
    # @pytest.mark.parametrize('data',get_yaml_data(os.path.join(config_path,'writeData.yml')))
    # def test_write(self,data):
    #     res = Wq().write(data)
    #     return res

    @pytest.mark.parametrize('quData',get_yaml_data2(os.path.join(config_path,'queryData.yml')))
    def test_query(self,quData):
        resp = Wq().query(quData)
        return resp


    #     return respon.text
    # #
    # def pull_data(self):
    #     listdata = []
    #
    #     pass

if __name__ == '__main__':
    pytest.main(['test_write2.py','-s'])