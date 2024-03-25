# To register, use the code below and replace with your login info
import requests
import os
from dotenv import load_dotenv
load_dotenv()

register_url = 'https://api.watttime.org/register'
params = {'username': os.getenv('WATT_TIME_USERNAME'),
         'password': os.getenv('WATT_TIME_PASSWORD'),
         'email': os.getenv('WATT_TIME_EMAIL'),
         'org': os.getenv('WATT_TIME_ORG'),}
rsp = requests.post(register_url, json=params)
print(rsp.text)