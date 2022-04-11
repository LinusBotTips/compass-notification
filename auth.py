import requests, os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
subdomain = os.getenv('SUBDOMAIN')
input("Add your subdomain to .env file before running!")
username = input("Compass Username: ")
password = input("Compass Password: ")

burp0_url = f"https://{subdomain}.compass.education:443/services/admin.svc/AuthenticateUserCredentials"
burp0_headers = {"Accept": "*/*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "iOS/14_6_0 type/iPhone CompassEducation/6.3.0", "Accept-Language": "en-au"}
burp0_json={"password": password, "sessionstate": "readonly", "username": username}
req = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
print(req.json()['d']['roles'][0]['userId'], "<< This is your UserID. Copy and paste it into your .env file in 'USER_ID='.")
print(req.cookies['ASP.NET_SessionId'].replace("'", ""), "<< This is your Cookie. Copy and paste it into your .env file in 'COOKIE='.")