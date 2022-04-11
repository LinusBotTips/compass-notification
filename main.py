import os, requests
from twilio.rest import Client
from dotenv import load_dotenv
from datetime import date
from datetime import datetime

load_dotenv()

# Load variables from .env file
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_phone = os.getenv('FROM_PHONE')
to_phone = os.getenv('TO_PHONE')
cookie = os.getenv('COOKIE')
user_id = os.getenv('USER_ID')
subdomain = os.getenv('SUBDOMAIN')
client = Client(account_sid, auth_token)
todays_date = date.today().strftime(f"%d/%m/%Y")

# Login to compass
burp0_cookies = {"ASP.NET_SessionId": "0516ba6c-69e2-4cf4-b25d-cf2af986f93a"}
burp0_url = f"https://{subdomain}.compass.education:443/services/mobile.svc/GetScheduleLinesForDate?sessionstate=readonly"
burp0_headers = {"Accept": "*/*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "iOS/14_6_0 type/iPhone CompassEducation/6.3.0", "Accept-Language": "en-au", "Connection": "close"}
burp0_json={"date": f"{todays_date} - 12:00 am", "sessionstate": "readonly", "userId": int(user_id)}
classes = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json).json()['d']['data']

# Get classes
if not classes:
    print("No classes today",)
else:
    timetable = {}
    for classobj in classes:
        # Converting 12 hour time to 24 hour time using datetime
        time = classobj['topTitleLine'].split(" - ")[0]
        in_time = datetime.strptime(time, "%I:%M %p")
        out_time = datetime.strftime(in_time, "%H:%M")
        
        # Get class name
        class_name = classobj['topTitleLine'].split(" - ")[1]

        # Add to json
        timetable[class_name + " - " + out_time + "\n"] = out_time

    # Send text
    message = client.messages.create(
        body=' '.join(sorted(timetable, key=timetable.get)),
        from_=from_phone,
        to=to_phone
    )

    print("Message sent! -", message.sid)