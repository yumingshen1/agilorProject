from common.baseApi import baseApi
from configs.config import indata

class Write(baseApi):
    def write(self,inData):
        respdata = self.request_send(data=inData)   ##请求发送数据
        return respdata




    def query(self):
        pass


if __name__ == '__main__':
    print(Write().write(indata))