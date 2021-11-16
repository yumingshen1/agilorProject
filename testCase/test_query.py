import requests
import json

def test_QueryData():
  url = "http://192.168.220.134:8713/agilorapi/v6/query"

  payload = json.dumps({
    "db": "agilor_test",
    "start": "-1h",
    "table": "cpu_usage5"
  })
  headers = {
    'Authorization': 'Token XXX',
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)
