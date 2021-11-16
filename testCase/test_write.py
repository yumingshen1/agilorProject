import requests

def test_WriteData():
  url = "http://192.168.220.134:8713/agilorapi/v6/write?db=我是数据库20"

  payload = "cpu_usage5,region=beijing,host=server1 core=7,usage=123"

  headers = {'Authorization': 'Token XXX','Content-Type': 'text/plain'}

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)


if __name__ == '__main__':
    test_WriteData()