import os
import requests
from base64 import b64encode
from dotenv import load_dotenv


load_dotenv()
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')

auth = b64encode(f'{consumer_key}:{consumer_secret}'.encode('utf8')).decode()

url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

payload = ''

headers = {
    "Authorization": f"Basic {auth}"
}
print(headers)

response = requests.get(url, headers= headers, data= payload)
print(response)
print(response.text)