import requests

TOKEN = 'YOUR API TOKEN'

server = 'https://api.telegram.org'
endpoint = 'getMe'

url = f'{server}/{TOKEN}/{endpoint}'

response = requests.get(url)
if response.status_code == 200:
    print(response.json())
else:
    print('err')
