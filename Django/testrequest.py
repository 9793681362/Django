import requests

url = 'http://127.0.0.1:8000/api/test_data/'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
