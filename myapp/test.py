import requests
import json

# 请求体数据
data = {
    'username': 'example_user',
    'password': 'example_password',
    'email': 'example@example.com',
    'phone_number':'17317795766'
}

# 发送 POST 请求
response = requests.post('http://127.0.0.1:8000/api/create_user', data=json.dumps(data), headers={'Content-Type': 'application/json'})
''

# 打印响应内容
print(response.status_code)
print(response.json())