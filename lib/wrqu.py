import requests
import json
from common.baseApi import BaseApi
from configs.config import indata
from configs.config import payload

class Wq(BaseApi):

  def write(self,data):
    res = self.request_send(data=data)
    # print('>>>>>>>',res.text)
    return res

  def query(self,quData):
    respon = self.request_send(data=quData)
    # print(type(respon.text))
    print(respon.text)
    return respon.text


if __name__ == '__main__':
    # print(Wq().write(indata))
    Wq().query(payload)