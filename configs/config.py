url = "http://192.168.220.150:8713/agilorapi/v6/query"
data = {
    "db": "PI",
    "start": "2021-01-13T05:00:00.000000001Z",
    "stop": "2021-12-13T05:00:00.000000001Z",
    "table": "PI_TABLE",
    "tags": [
        {
            "AGPOINTNAME": "sy.st.WIN-F9KROVHMQ74.random1.DeviceStatus"
        }
    ]
}
headers = {
    'Authorization': 'Token XXX',
    'Content-Type': 'application/json'
}