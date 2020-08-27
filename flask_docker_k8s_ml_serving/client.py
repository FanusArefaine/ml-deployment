import requests
import json

# insert here the URL given from the Kubernetes with the extension /api
url = 'http://34.71.91.206/api'

# the input data
data = [[14.34, 1.68, 2.7, 25.0]]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)