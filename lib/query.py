import requests
import json

def test_QueryData(): ##查询接口
  url = "http://192.168.220.134:8713/agilorapi/v6/query"
  payload = json.dumps({
    "db": "agilor_test",
    "start": "2021-11-18T08:51:00.1634864721Z",
    "table": "cpu_usage_func11",
    "tags": [
      {
        "AGPOINTNAME": "Simu1_1"
      }
    ]
  })

  headers = {
    'Authorization': 'Token XXX',
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)
  print(type(response.text))  ##查询后得到str类型的多条数据
  return response

def countlist():  ##获取查询接口的数据，并处理数据
  tq = test_QueryData()
  list = []
  for i in range(len(tq)):
    list.append(i)
  print(list)


if __name__ == '__main__':
    test_QueryData()
    # countlist()
