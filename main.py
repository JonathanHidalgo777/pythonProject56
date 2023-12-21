import requests
import json

import urllib3

http = urllib3.PoolManager()
urllib3.disable_warnings()

url = "https://10.10.20.14/api/aaaLogin.json"
data = {
    "aaaUser" : {
        "attributes" : {
            "name" : "admin",
            "pwd" : "C1sco12345"
        }
    }
}
cabecera = {"content-type":"application/json"}
respuesta = requests.post(url, json.dumps(data),  headers=cabecera, verify=False)
respuesta_json = respuesta.json()


print(respuesta_json)

