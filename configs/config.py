import json

HOST = 'http://192.168.220.134:8713'
indata = "cpu_usage5,region=beijing,host=server1 core=0,usage=7788"

payload = json.dumps({
    "db": "agilor_test",
    "start": "2021-11-18T01:00:00.1634864721Z",
    "table": "cpu_usage5"
})
