import requests
import json

URL = 'http://127.0.0.1:8000/api/student-create/'

data = {
    'name':'Harun Rai',
    'roll': 11,
    'city': 'Itahari'
}

json_data = json.dumps(data)

r = requests.post(url=URL, data = json_data)

r_data = r.json()
print(r_data)

