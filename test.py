import datetime
from pytz import timezone
import requests

params = {
    'limit': 100,
    'https': 'true'
}

response = requests.get('http://localhost:8899/api/v1/proxies', params=params)
proxy_list = ['{}:{}'.format(proxy['ip'], proxy['port']) for proxy in response.json()['proxies']]

japan = timezone('Japan')
japan_now = datetime.datetime.now(japan)
#'20190227'
print('{}{:02d}{}'.format(japan_now.year, japan_now.month, japan_now.day))

print('!')