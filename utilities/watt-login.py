# To login and obtain an access token, use this code:

import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
load_dotenv()

WATT_TIME_USERNAME = os.getenv('WATT_TIME_USERNAME')
WATT_TIME_PASSWORD = os.getenv('WATT_TIME_PASSWORD')


login_url = 'https://api.watttime.org/login'
rsp = requests.get(login_url, auth=HTTPBasicAuth(WATT_TIME_USERNAME,WATT_TIME_PASSWORD))
TOKEN = rsp.json()['token']
print(rsp.json())